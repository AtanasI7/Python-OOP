from project.product import Product


class Drink(Product):
    DEFAULT_QUANTITY = 10

    def __init__(self, name: str):
        Product.__init__(self, name, self.DEFAULT_QUANTITY)
