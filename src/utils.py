import json
import os

from src.models import Category, Product


def read_json(path: str) -> list[dict]:
    """Функция принимает путь к json файлу и открывает его"""
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF-8") as file:
        data = json.load(file)
    return data


def create_objects_from_json(data):
    """Функция создает объекты из json файла"""
    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))
    return categories
