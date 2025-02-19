import unittest
from unittest import TestCase


class MyCar:

    def __init__(self, model: str, hp: int):
        self.model = model
        self.hp = hp


#Test suite
class TestMyCar(TestCase):

    def test_correct_init(self):
        model, hp = "BMW", 100 # Arrange
        my_car = MyCar(model, hp) # Act

        # my_car = MyCar("BMW", 100) # Arrange & Act


        self.assertEqual(my_car.model, model)
        self.assertEqual(my_car.hp, hp)

