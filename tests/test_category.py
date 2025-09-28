import pytest


def test_category_init(first_category, second_category):
    # тестируем первую категорию
    assert first_category.name == "Овощи"
    assert first_category.description == "Подходят для приготовления салатов и сложных блюд"
    assert len(first_category.products_in_list) == 2
    assert first_category.category_count == 2
    # тестируем вторую категорию
    assert second_category.name == "Фрукты"
    assert second_category.description == "Подходят для приготовления закусок и употребления в сыром виде"
    assert len(second_category.products_in_list) == 3
    assert second_category.category_count == 2


def test_category_property(first_category):
    assert first_category.products == "Помидоры, 250 руб. Остаток: 100 шт.\nПомидоры, 260 руб. Остаток: 120 шт.\n"


def test_category_setter(first_category, product):
    # изначальное количество продуктов в листе
    assert len(first_category.products_in_list) == 2
    # добавляем продукт в лист
    first_category.products = product
    # проверяем добавился ли продукт в лист
    assert len(first_category.products_in_list) == 3


def test_category_str(first_category):
    assert str(first_category) == "Овощи, количество продуктов: 220 шт."


def test_product_iterator(product_iterator):
    iter(product_iterator)  # проверяем переопределение итерации
    assert product_iterator.index == 0
    assert next(product_iterator).name == "Банан"
    assert next(product_iterator).name == "Мандарин"
    assert next(product_iterator).name == "Яблоко"
    # проверяем возбуждение ошибки StopIteration
    with pytest.raises(StopIteration):
        next(product_iterator)
