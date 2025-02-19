from unittest import TestCase, main
from project.mammal import Mammal


class TestMammal(TestCase):

    def setUp(self):
        self.mammal = Mammal("Rex", "dog", "rawr")

    def test_correct_init(self):
        self.assertEqual("Rex", self.mammal.name)
        self.assertEqual("dog", self.mammal.type)
        self.assertEqual("rawr", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound_return_name_and_sound(self):
        self.assertEqual("Rex makes rawr", self.mammal.make_sound())

    def test_get_kingdom_returns_kingdom(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_info_returns_info(self):
        self.assertEqual("Rex is of type dog", self.mammal.info())

if __name__ == "__main__":
    main()