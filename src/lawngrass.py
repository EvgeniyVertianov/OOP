from src.product import Product


class LawnGrass(Product):
    """Класс предоставляет продукт - Трава газонная"""

    # страна производитель
    country: str
    # срок прорастания
    germination_period: str
    # цвет
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        if type(other) is LawnGrass:
            total = self.quantity * self.price + other.quantity * other.price
            return total
        raise TypeError
