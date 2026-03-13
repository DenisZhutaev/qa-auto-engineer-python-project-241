# gendiff.scripts.core module

from gendiff.formatters import format_diff
from gendiff.scripts.parsers import parse_file


def build_diff_tree(first_data, second_data):
    all_keys = sorted(set(first_data.keys()) | set(second_data.keys()))
    diff_tree = {}

    for key in all_keys:
        first_value = first_data.get(key)
        second_value = second_data.get(key)

        if key not in first_data:
            diff_tree[key] = {'status': 'added', 'value': second_value}
        elif key not in second_data:
            diff_tree[key] = {'status': 'removed', 'value': first_value}
        elif first_value != second_value:
            diff_tree[key] = {
                'status': 'changed',
                'old_value': first_value,
                'new_value': second_value
            }
        else:
            diff_tree[key] = {'status': 'unchanged', 'value': first_value}

    return diff_tree


def generate_diff(first_file, second_file, format_name='stylish'):
    first_data = parse_file(first_file)
    second_data = parse_file(second_file)

    diff_tree = build_diff_tree(first_data, second_data)

    return format_diff(diff_tree, format_name)
