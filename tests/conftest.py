import pytest

from src.models import Category, Product


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
