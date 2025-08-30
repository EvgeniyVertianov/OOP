def test_category_init(first_category, second_category):
    # тестируем первую категорию
    assert first_category.name == "Овощи"
    assert first_category.description == "Подходят для приготовления салатов и сложных блюд"
    assert len(first_category.products) == 2
    assert first_category.category_count == 2
    # тестируем вторую категорию
    assert second_category.name == "Фрукты"
    assert second_category.description == "Подходят для приготовления закусок и употребления в сыром виде"
    assert len(second_category.products) == 3
    assert second_category.category_count == 2
