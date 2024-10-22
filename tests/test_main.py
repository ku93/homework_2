import pytest

from main import Category, Product


@pytest.fixture
def product():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def category(product):
    return Category("Смартфоны", "Смартфоны, как средство не только коммуникации", [product])


def test_product_init(product):
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_category_init(category):
    assert category.name == "Смартфоны"
    assert category.description == "Смартфоны, как средство не только коммуникации"


def test_add_product_and_count(category, product):
    """Тест на добавление продукта в категорию и подсчет продуктов."""
    category.add_product(product)  # Добавляем продукт
    assert len(category.products) == 1  # Проверяем, что продукт добавлен


def test_total_products(category):
    """Тест на общее количество продуктов в категории."""
    assert len(category.products) == 0  # Проверяем, что в категории 1 продукт
