from project.gallery import Gallery
from unittest import TestCase, main

class TestGallery(TestCase):

    def setUp(self):
        self.gallery = Gallery("ART", "Plovdiv", 100)

    def test_correct_init(self):
        self.assertEqual("ART", self.gallery.gallery_name)
        self.assertEqual("Plovdiv", self.gallery.city)
        self.assertEqual(100, self.gallery.area_sq_m)

    def test_gallery_name_when_name_contains_symbol_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.gallery.gallery_name = "A-RT"

        self.assertEqual("Gallery name can contain letters and digits only!", str(ve.exception))

    def test_city_when_city_starts_with_digit(self):
        with self.assertRaises(ValueError) as ve:
            self.gallery.city = "4Plovdiv"

        self.assertEqual("City name must start with a letter!", str(ve.exception))

    def test_area_when_area_is_negative(self):
        with self.assertRaises(ValueError) as ve:
            self.gallery.area_sq_m = -1

        self.assertEqual("Gallery area must be a positive number!", str(ve.exception))

    def test_add_exhibition_when_exhibition_doesnt_exists(self):
        expected_result = self.gallery.add_exhibition("Ivan", 1989)
        self.assertEqual(f'Exhibition "Ivan" added for the year 1989.', expected_result)

    def test_add_exhibition_when_already_exists(self):
        self.gallery.add_exhibition("Ivan", 1989)
        expected_result = self.gallery.add_exhibition("Ivan", 1989)

        self.assertEqual('Exhibition "Ivan" already exists.', expected_result)

    def test_remove_exhibition_when_exhibition_exists(self):
        self.gallery.add_exhibition("Ivan", 1989)
        expected_result = self.gallery.remove_exhibition("Ivan")

        self.assertEqual('Exhibition "Ivan" removed.', expected_result)

    def test_remove_exhibition_when_exhibition_doesnt_exists(self):
        expected_result = self.gallery.remove_exhibition("Ivan")

        self.assertEqual('Exhibition "Ivan" not found.', expected_result)

    def test_list_exhibition_when_is_open_to_public(self):
        self.gallery.add_exhibition("Ivan", 1989)
        self.gallery.add_exhibition("Petar", 2000)
        expected_result = self.gallery.list_exhibitions()

        self.assertEqual("Ivan: 1989\nPetar: 2000", expected_result)

    def test_list_exhibition_when_not_open_to_public(self):
        self.gallery.open_to_public = False
        expected_result = self.gallery.list_exhibitions()

        self.assertEqual('Gallery ART is currently closed for public! Check for updates later on.', expected_result)

if __name__ == "__main__":
    main()