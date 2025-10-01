from src.product import Product


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

    @products.setter
    def products(self, product: Product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products_in_list(self):
        return self.__products
