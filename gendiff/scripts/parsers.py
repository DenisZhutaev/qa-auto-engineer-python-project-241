# gendiff.parsers module

import json

import yaml


def parse_file(filepath):
    with open(filepath) as f:
        if filepath.endswith(('.yaml', '.yml')):
            return yaml.safe_load(f)
        elif filepath.endswith('.json'):
            return json.load(f)
        raise ValueError(f'Unsupported file format: {filepath}')
