from src.products import Product

class Category:
    """Класс для категорий"""

    # Атрибуты класса для хранения общей информации
    total_categories = 0  # Общее количество категорий
    total_products = 0  # Общее количество товаров

    name: str
    description: str
    products: list

    def __init__(self, name, description, products):
        self.name = name  # Название категории
        self.description = description  # Описание категории
        self.products = []  # Список товаров категории
        self.total_products = 0  # Количество товаров в данной категории
        # Увеличиваем общее количество категорий
        Category.total_categories += 1

    def add_product(self, product: Product):
        """Метод для добавления товара в категорию."""
        if isinstance(product, Product):
            self.products.append(product)
            Category.total_products += (
                product.quantity
            )  # Увеличиваем общее количество продуктов на указанное количество
            print(f"Добавлен {product.name} в категорию '{self.name}' (количество: {product.quantity}).")
        else:
            print("Ошибка: В объекте должен быть тип Product.")

    def __len__(self):
        """Метод для возвращения количества продуктов в категории."""
        return sum(product.quantity for product in self.products)

    def get_product_count(self):
        """Метод для получения общего количества продуктов в категории."""
        return len(self)

    def __str__(self):
        return f"Category(name={self.name}, description={self.description}, number of products={self.get_product_count()})"






if __name__ == "__main__":

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)

    category1 = Category("Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    category1.add_product(product1)
    category1.add_product(product2)
    category1.add_product(product3)

    print(category1.name)
    print(category1.description)
    print(len(category1.products))
    print(category1.total_categories)
    print(category1.total_products)


    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product4],
    )
    category2.add_product(product4)

    print(category2.name)
    print(category2.description)
    print(len(category2.products))

    print(Category.total_categories)
    print(Category.total_products)