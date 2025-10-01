import json

from src.category import Category
from src.utils import create_objects_from_json, read_json


def test_read_valid_json_list_of_dicts(json_file):
    """
    Функция тестирует чтение корректного JSON-файла, содержащего список словарей.
    """
    expected_data = [{"id": 1, "name": "Item A", "value": 100}, {"id": 2, "name": "Item B", "value": 200}]
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(expected_data, f)

    actual_data = read_json(str(json_file))
    assert actual_data == expected_data


def test_read_valid_json_empty_list(json_file):
    """
    Функция тестирует чтение корректного JSON-файла, содержащего пустой список.
    """
    expected_data = []
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(expected_data, f)

    actual_data = read_json(str(json_file))
    assert actual_data == expected_data


def test_create_objects_from_json_valid_data(sample_data):
    """Тестирует функцию create_objects_from_json с корректными данными из фикстуры."""
    result = create_objects_from_json(sample_data)
    assert len(result) == 2
    assert isinstance(result[0], Category)
    assert result[0].name == "Смартфоны"
    assert result[1].name == "Телевизоры"
