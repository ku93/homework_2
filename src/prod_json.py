import json


class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def to_dict(self):
        """Метод для преобразования объекта Product в словарь."""
        return {"name": self.name, "description": self.description, "price": self.price, "quantity": self.quantity}


class Category:
    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.products = products if products is not None else []

    def add_product(self, product):
        """Метод для добавления продукта в категорию."""
        self.products.append(product)

    def to_dict(self):
        """Метод для преобразования объекта Category в словарь."""
        return {
            "name": self.name,
            "description": self.description,
            "products": [product.to_dict() for product in self.products],
        }


# Создаем продукты для категории "Смартфоны"
smartphone1 = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
smartphone2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
smartphone3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

# Создаем категорию "Смартфоны" и добавляем продукты
smartphones_category = Category(
    "Смартфоны",
    "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
    [smartphone1, smartphone2, smartphone3],
)

# Создаем продукты для категории "Телевизоры"
tv1 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)

# Создаем категорию "Телевизоры" и добавляем продукт
tv_category = Category(
    "Телевизоры",
    "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
    [tv1],
)

# Объединяем категории в список
categories = [smartphones_category, tv_category]

# Сериализация в JSON
categories_json = json.dumps([category.to_dict() for category in categories], ensure_ascii=False, indent=4)

# Выводим JSON
print(categories_json)
