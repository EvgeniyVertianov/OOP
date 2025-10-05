import pytest

from src.product import Product


def test_product_init(product):
    assert product.name == "Мандарин"
    assert product.description == "Сорт «Клементин»"
    assert product.price == 200
    assert product.quantity == 400


def test_product_create():
    product = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product.name = "Iphone 15"
    product.description = "512GB, Gray space"
    product.price = 210000.0
    product.quantity = 8


def test_new_product():
    Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    assert Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


def test_add_product(product, empty_category):
    # изначальное количество товаров в категории должно быть 0
    assert len(empty_category.products_in_list) == 0
    # добавляем продукт в категорию
    empty_category.add_product(product)
    # проверяем, что количество товаров в категории увеличилось на 1
    assert len(empty_category.products_in_list) == 1


def test_product_price_update(capsys, product):
    # реализуем отрицательный исход
    product.price = 0
    # реализуем перехват сообщения с помощью capsys
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-1] == "Цена не должна быть нулевая или отрицательная"
    # реализуем положительный исход
    product.price = 200
    assert product.price == 200


def test_product_str(product):
    assert str(product) == "Мандарин, 200 руб. Остаток: 400 шт."


def test_product_add(product_for_add1, product_for_add2):
    assert product_for_add1 + product_for_add2 == 146000


def test_product_add_error(product_for_add1):
    with pytest.raises(TypeError):
        assert product_for_add1 + 1
