# gendiff.formatters.stylish module


def _format_value(value):
    if value is True:
        return 'true'
    if value is False:
        return 'false'
    if value is None:
        return 'null'
    return str(value)


def format_stylish(diff_tree):
    lines = ['{']
    lines.extend(build_stylish(diff_tree, indent=2))
    lines.append('}')
    return '\n'.join(lines)


def build_stylish(diff_tree, indent=2):
    lines = []
    indent_str = ' ' * indent

    for key, value in diff_tree.items():
        if isinstance(value, dict) and 'status' in value:
            status = value['status']

            if status == 'removed':
                lines.append(
                    f'{indent_str}- {key}: {_format_value(value.get("value"))}'
                )
            elif status == 'added':
                lines.append(
                    f'{indent_str}+ {key}: {_format_value(value.get("value"))}'
                )
            elif status == 'unchanged':
                lines.append(
                    f'{indent_str}  {key}: {_format_value(value.get("value"))}'
                )
            elif status == 'changed':
                lines.append(
                    f'{indent_str}- {key}: '
                    f'{_format_value(value.get("old_value"))}'
                )
                lines.append(
                    f'{indent_str}+ {key}: '
                    f'{_format_value(value.get("new_value"))}'
                )
        else:
            lines.append(f'{indent_str}  {key}: {value}')

    return lines
