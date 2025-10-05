from src.baseproduct import BaseProduct


class Product(BaseProduct):
    """Класс предоставляет продукт"""

    # название
    name: str
    # описание
    description: str
    # цена
    # price: float - закомитил так как использую @property. Mypy ругается
    # количество в наличии
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if isinstance(other, Product):
            total = self.quantity * self.__price + other.quantity * other.price
            return total
        else:
            raise TypeError

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
