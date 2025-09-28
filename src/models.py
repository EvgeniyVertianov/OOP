class Product:
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
            raise ValueError("Невозможно сложить объекты разных типов")

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
    # products: list[Product] - закомитил так как использую @property. Mypy ругается
    # количество категорий
    category_count: int = 0
    # количество товаров
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        self.name = name
        self.description = description
        self.__products = products if products is not None else []
        # вычисляем количество категорий
        Category.category_count += 1
        # вычисляем количество продуктов
        Category.product_count += len(products)

    def __str__(self):
        total_quantity = 0
        for product in self.__products:
            total_quantity += product.quantity
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product: Product):
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        products_str = ""
        for product in self.__products:
            products_str += f"{str(product)}\n"
        return products_str

    # @property
    # def products(self):
    #     return str(Product)

    @products.setter
    def products(self, product: Product):
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products_in_list(self):
        return self.__products
