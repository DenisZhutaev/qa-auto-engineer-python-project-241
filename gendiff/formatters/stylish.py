# gendiff.formatters.stylish module


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
                lines.append(f'{indent_str}- {key}: {value.get("value")}')
            elif status == 'added':
                lines.append(f'{indent_str}+ {key}: {value.get("value")}')
            elif status == 'unchanged':
                lines.append(f'{indent_str}  {key}: {value.get("value")}')
            elif status == 'changed':
                lines.append(f'{indent_str}- {key}: {value.get("old_value")}')
                lines.append(f'{indent_str}+ {key}: {value.get("new_value")}')
        else:
            lines.append(f'{indent_str}  {key}: {value}')

    return lines
