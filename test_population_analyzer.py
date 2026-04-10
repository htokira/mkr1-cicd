import pytest
from population_analyzer import read_population_data, calculate_population_change


@pytest.fixture
def create_test_file(tmp_path):
    """Фікстура для створення тимчасових файлів даних."""
    def _create(content):
        p = tmp_path / "temp_data.txt"
        p.write_text(content, encoding="utf-8")
        return str(p)
    return _create


@pytest.mark.parametrize("content, expected", [
    ("Ukraine, 2020, 41000\nUkraine, 2021, 40000", {"Ukraine": {2020: 41000, 2021: 40000}}),
    ("Poland, 2019, 38000", {"Poland": {2019: 38000}}),
    ("", {}),
])
def test_read_population_data(create_test_file, content, expected):
    file_path = create_test_file(content)
    assert read_population_data(file_path) == expected


@pytest.mark.parametrize("input_data, expected_changes", [
    (
        {"Ukraine": {2020: 41000, 2021: 40000}},
        {"Ukraine": {"2020-2021": -1000}}
    ),
    (
        {"USA": {2010: 300, 2020: 330}},
        {"USA": {"2010-2020": 30}}
    ),
    (
        {"Norway": {2021: 5000}},
        {"Norway": {}}
    )
])
def test_calculate_population_change(input_data, expected_changes):
    assert calculate_population_change(input_data) == expected_changes
