from typing import Any


class Product:
    """Класс предоставляет продукт"""

    # название
    name: str
    # описание
    description: str
    # цена
    price: float
    # количество в наличии
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """Класс предоставляет категорию продукта"""

    # название
    name: str
    # описание
    description: str
    # список товаров категории Product
    products: list[Product]
    # количество категорий
    category_count: int = 0
    # количество товаров
    product_count: int = 0

    def __init__(self, name: str, description: str, products: Any):
        self.name = name
        self.description = description
        self.products = products if products is not None else []
        # вычисляем количество категорий
        Category.category_count += 1
        # вычисляем количество продуктов
        Category.product_count = len(products)
