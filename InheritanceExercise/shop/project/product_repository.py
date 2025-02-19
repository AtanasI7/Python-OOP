from itertools import product
from typing import List
from project.drink import Drink
from project.food import Food


class ProductRepository:

    def __init__(self):
        self.products: List[Drink, Food] = []

    def add(self, product: Food or Drink):
        self.products.append(product)

    def find(self, product_name: str):
        # try:
        #     product = next(filter(lambda p: p.name == product_name, self.products))
        #     return product
        # except StopIteration:              !!!!! И ДВАТА НАЧИНА РАБОТЯТ !!!!!
        #     pass

        for product in self.products:
             if product.name == product_name:
                 return product

    def remove(self, product_name):
        product = self.find(product_name)

        if product:
            self.products.remove(product)

    def __repr__(self):
        return "\n".join(f"{p.name}: {p.quantity}" for p in self.products)