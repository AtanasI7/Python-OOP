from project.animals.animal import Bird
from project.food import Meat, Vegetable, Fruit, Seed


class Owl(Bird):
    
    @property
    def food_that_eats(self):
        return [Meat]
    
    @property
    def gained_weight(self):
        return 0.25

    @staticmethod
    def make_sound():
        return f"Hoot Hoot"

class Hen(Bird):

    @property
    def food_that_eats(self):
        return [Meat, Vegetable, Fruit, Seed]

    @property
    def gained_weight(self):
        return 0.35

    @staticmethod
    def make_sound():
        return f"Cluck"

