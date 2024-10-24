import pytest
from src.category import Category
from src.products import Product

@pytest.fixture
def product():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def category(product):
    return Category("Смартфоны", "Смартфоны, как средство не только коммуникации", [product])

def test_category_init(category):
    assert category.name == "Смартфоны"
    assert category.description == "Смартфоны, как средство не только коммуникации"


def test_add_product_and_count(category, product):
    """Тест на добавление продукта в категорию и подсчет продуктов."""
    # Убедимся, что в начале в категории только один продукт
    assert len(category.products) == 0   # Добавляем новый продукт
    new_product = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    category.add_product(new_product)  # Добавляем новый продукт # Проверяем, что теперь в категории 2 продукта
    assert len(category.products) == 1


def test_total_products(category):
    """Тест на общее количество продуктов в категории."""
    assert len(category.products) == 0  # Проверяем, что в категории 1 продукт
