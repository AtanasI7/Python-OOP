from unittest import TestCase, main
from task3Test.movie import Movie


class TestMovie(TestCase):

    def setUp(self):
        self.movie = Movie("Infinity war", 2018, 7.8)

    def test_correct_init(self):
        self.assertEqual("Infinity war", self.movie.name)
        self.assertEqual(2018, self.movie.year)
        self.assertEqual(7.8, self.movie.rating)

    





if __name__ == "__main__":
    main()
