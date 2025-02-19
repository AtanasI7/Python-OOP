from project.animals.animal import Mammal
from project.food import Fruit, Vegetable, Meat


class Mouse(Mammal):

    @property
    def food_that_eats(self):
        return [Fruit, Vegetable]

    @property
    def gained_weight(self):
        return 0.10

    @staticmethod
    def make_sound():
        return f"Squeak"

class Dog(Mammal):

    @property
    def food_that_eats(self):
        return [Meat]

    @property
    def gained_weight(self):
        return 0.40

    @staticmethod
    def make_sound():
        return f"Woof!"

class Cat(Mammal):

    @property
    def food_that_eats(self):
        return [Meat, Vegetable]

    @property
    def gained_weight(self):
        return 0.30

    @staticmethod
    def make_sound():
        return f"Meow"

class Tiger(Mammal):

    @property
    def food_that_eats(self):
        return [Meat]

    @property
    def gained_weight(self):
        return 1.00

    @staticmethod
    def make_sound():
        return f"ROAR!!!"
