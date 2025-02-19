from unittest import TestCase, main

#from Task_3.extended_list import IntegerList


class TestIntegerList(TestCase):

    def setUp(self):
        self.i_list = IntegerList(5.5, 1, 2, 3, "hello")

    def test_correct_init_ignores_not_int_element(self):
        self.assertEqual([1, 2, 3], self.i_list.get_data())

    def test_add_element_in_list_not_int_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.i_list.add('lele')

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_add_int_adds_int_to_the_list(self):
        expected_list = self.i_list.get_data().copy() + [4]

        self.i_list.add(4)

        self.assertEqual(expected_list, self.i_list.get_data())

    def test_remove_index_index_out_of_range_raises_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.i_list.remove_index(10000)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_remove_index_index_is_valid_get_index_remove_index(self):
        self.i_list.remove_index(0)

        self.assertEqual([2, 3], self.i_list.get_data())

    def test_get_index_out_of_range_raises_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.i_list.get(10000)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_get_with_valid_index_returns_value_on_index(self):
        result = self.i_list.get(1)

        self.assertEqual(2, result)

    def test_insert_index_out_of_range_raises_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.i_list.insert(1000, 5)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_element_is_not_int_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.i_list.insert(0, 'hero')

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_insert_int_on_valid_index(self):
        expected_list = self.i_list.get_data().copy()
        expected_list.insert(1, 3)

        self.i_list.insert(1, 3)

        self.assertEqual(expected_list, self.i_list.get_data())

    def test_get_biggest_number(self):
        result = self.i_list.get_biggest()

        self.assertEqual(3, result)

    def test_get_index_(self):
        result = self.i_list.get_index(1)

        self.assertEqual(0, result)




if __name__ == "__main__":
    main()