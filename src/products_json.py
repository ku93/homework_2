import json

from main import Category, Product

with open("../data/products.json",  encoding="utf-8") as file:
    data = json.load(file)

def __init__(self, name, description, products):
    self.Category.name = data["name"]
    self.Category.description = data["description"]
    self.Category.products = data["products"]


