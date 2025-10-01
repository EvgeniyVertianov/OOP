import pytest

from src.category import Category
from src.lawngrass import LawnGrass
from src.product import Product
from src.product_iterator import ProductIterator
from src.smartphone import Smartphone


@pytest.fixture
def first_category():
    return Category(
        name="Овощи",
        description="Подходят для приготовления салатов и сложных блюд",
        products=[Product("Помидоры", "Черри - красные", 250, 100), Product("Помидоры", "Черри - желтые", 260, 120)],
    )


@pytest.fixture
def second_category():
    return Category(
        name="Фрукты",
        description="Подходят для приготовления закусок и употребления в сыром виде",
        products=[
            Product("Банан", "Сорт «Кавендиш» ", 220, 300),
            Product("Мандарин", "Сорт «Клементин»", 200, 400),
            Product("Яблоко", "Сорт «Редчиф»", 280, 500),
        ],
    )


@pytest.fixture
def product():
    return Product("Мандарин", "Сорт «Клементин»", 200, 400)


@pytest.fixture
def empty_category():
    """Фикстура для создания пустой категории"""
    return Category("Тестовая категория", "пустая категория", [])


@pytest.fixture
def product_iterator(second_category):
    return ProductIterator(second_category)


@pytest.fixture
def product_for_add1():
    return Product("Банан", "Сорт «Кавендиш» ", 220, 300)


@pytest.fixture
def product_for_add2():
    return Product("Мандарин", "Сорт «Клементин»", 200, 400)


@pytest.fixture
def smartphone_1():
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture
def smartphone_2():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def lawngrass_1():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def lawngrass_2():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
