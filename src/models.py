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
        self.__price = price
        self.quantity = quantity


    @classmethod
    def new_product(cls, product):
            return cls(**product)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: int):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return



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
        self.__products = products if products is not None else []
        # вычисляем количество категорий
        Category.category_count += 1
        # вычисляем количество продуктов
        Category.product_count = len(products)

    def add_product(self, product: Product):
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        products_str = ""
        for product in self.__products:
            products_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_str
