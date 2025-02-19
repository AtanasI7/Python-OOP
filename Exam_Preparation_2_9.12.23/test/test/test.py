from collections import deque
from unittest import TestCase, main
from project.railway_station import RailwayStation


class TestRailwayStation(TestCase):

    def setUp(self):
        self.station = RailwayStation("Sofia")

    def test_correct_init(self):
        self.assertEqual("Sofia", self.station.name)
        self.assertEqual(deque(), self.station.arrival_trains)
        self.assertEqual(deque(), self.station.departure_trains)

    def test_name_when_name_has_less_chars_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.station.name = "So"

        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.station.name = "Sof"

        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))

    def test_new_arrival_on_board_expect_success(self):
        self.station.new_arrival_on_board("Sofia-Plovdiv")

        self.assertEqual(deque(["Sofia-Plovdiv"]), self.station.arrival_trains)

    def test_train_has_arrived_expect_success(self):
        self.station.arrival_trains.append('some info')
        result = self.station.train_has_arrived('another info')

        self.assertEqual(f"There are other trains to arrive before another info.", result)

    def test_train_has_arrived_when_no_arrived_trains(self):
        self.station.arrival_trains.append('some info') #0
        self.station.arrival_trains.append('another info') #1
        result = self.station.train_has_arrived('some info')

        self.assertEqual(f"some info is on the platform and will leave in 5 minutes.", result)
        self.assertEqual(deque(['another info']), self.station.arrival_trains)
        self.assertEqual(deque(['some info']), self.station.departure_trains)

    def test_train_has_left_expect_success(self):
        self.station.departure_trains.append("some info")
        self.station.departure_trains.append("another info")

        result = self.station.train_has_left('some info')

        self.assertEqual(True, result)

    def test_train_has_left_failure_returns_false(self):
        self.station.departure_trains.append("some info")

        result = self.station.train_has_left('another info')

        self.assertEqual(False, result)
if __name__ == "__main__":
    main()