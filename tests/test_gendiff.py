from gendiff import generate_diff


def test_generate_diff_flat_json():
    first_file = 'tests/test_data/file1.json'
    second_file = 'tests/test_data/file2.json'
    expected_file = 'tests/test_data/expected_flat.json'

    with open(expected_file) as f:
        expected = f.read()

    result = generate_diff(first_file, second_file)
    assert result == expected


def test_generate_diff_flat_yaml():
    first_file = 'tests/test_data/file1.yml'
    second_file = 'tests/test_data/file2.yml'
    expected_file = 'tests/test_data/expected_flat.yml'

    with open(expected_file) as f:
        expected = f.read()

    result = generate_diff(first_file, second_file)
    assert result == expected


def test_generate_diff_flat_plain():
    first_file = 'tests/test_data/file1.json'
    second_file = 'tests/test_data/file2.json'
    expected_file = 'tests/test_data/expected_flat_plain.json'

    with open(expected_file) as f:
        expected = f.read()

    result = generate_diff(first_file, second_file, 'plain')
    assert result == expected


def test_generate_diff_json_format():
    first_file = 'tests/test_data/file1.json'
    second_file = 'tests/test_data/file2.json'
    expected_file = 'tests/test_data/expected_flat_json.json'

    with open(expected_file) as f:
        expected = f.read()

    result = generate_diff(first_file, second_file, 'json')
    assert result == expected
