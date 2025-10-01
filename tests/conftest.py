import pytest

from src.category import Category
from src.lawngrass import LawnGrass
from src.product import Product
from src.product_iterator import ProductIterator
from src.smartphone import Smartphone


@pytest.fixture
def json_file(tmp_path):
    """
    Фикстура Pytest, которая создает временный JSON-файл для каждого теста.
    `tmp_path` - это встроенная фикстура Pytest, предоставляющая временную директорию.
    """
    file_path = tmp_path / "test.json"
    return file_path


@pytest.fixture
def sample_data():
    "Фикстура для проверки функции create_objects_from_json"
    return [
        {
            "name": "Смартфоны",
            "description": "Средство коммуникации и получение дополнительных функций для удобства жизни",
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5,
                },
                {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8},
                {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14},
            ],
        },
        {
            "name": "Телевизоры",
            "description": "Современный телевизор",
            "products": [
                {"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}
            ],
        },
    ]


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
