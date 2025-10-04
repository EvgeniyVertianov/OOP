from src.product import Product


class Smartphone(Product):
    """Класс предоставляет продукт - смартфон"""

    # производительность
    efficiency: float
    # модель
    model: str
    # объем встроенной памяти
    memory: int
    # цвет
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        if isinstance(other, Smartphone):
            total = self.quantity * self.price + other.quantity * other.price
            return total
        raise TypeError
