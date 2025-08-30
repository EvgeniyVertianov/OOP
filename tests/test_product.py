def test_product_init(product):
    assert product.name == "Мандарин"
    assert product.description == "Сорт «Клементин»"
    assert product.price == 200
    assert product.quantity == 400
