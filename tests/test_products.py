import pytest
from src.products import Product


@pytest.fixture
def product():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

def test_product_init(product):
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5
    