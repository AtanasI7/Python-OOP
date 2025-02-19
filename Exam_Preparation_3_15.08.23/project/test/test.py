from unittest import TestCase, main
from project.trip import Trip


class TestTrip(TestCase):

    def setUp(self):
        self.trip = Trip(10000, 3, True)

    def test_correct_init(self):
        self.assertEqual(10000, self.trip.budget)
        self.assertEqual(3, self.trip.travelers)
        self.assertEqual(True, self.trip.is_family)

    def test_travelers_props_when_travelers_below_one_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.trip.travelers = 0

        self.assertEqual('At least one traveler is required!', str(ve.exception))

    def test_is_family_when_more_than_two_travelers(self):
        self.trip.travelers = 1
        self.trip.is_family = True

        self.assertEqual(False, self.trip.is_family)

    def test_is_family_when_value_false_but_more_than_two_people(self):
        self.trip.is_family = True

        self.assertEqual(True, self.trip.is_family)

    def test_book_a_trip_when_invalid_destination_returns_string(self):
        result = self.trip.book_a_trip("Romania")

        self.assertEqual('This destination is not in our offers, please choose a new one!', result)

    def test_book_a_trip_when_is_family_true_returns_string(self):
        self.trip.is_family = True
        result = self.trip.book_a_trip("Bulgaria")
        expected_price = 500 * self.trip.travelers * 0.9

        expected_booked_paid_amount = {"Bulgaria": expected_price}

        self.assertEqual(f'Successfully booked destination Bulgaria! Your budget left is 8650.00', result)
        self.assertEqual(expected_booked_paid_amount, self.trip.booked_destinations_paid_amounts)
        self.assertEqual(8650, self.trip.budget)

    def test_book_a_trip_when_no_budget_returns_string(self):
        self.trip.budget = 1
        result = self.trip.book_a_trip("Bulgaria")

        self.assertEqual('Your budget is not enough!', result)

    def test_booking_status_when_nothing_is_booked(self):
        result = self.trip.booking_status()

        self.assertEqual(f'No bookings yet. Budget: {self.trip.budget:.2f}', result)

    def test_booking_status_when_bulgaria_and_austria_trips_are_booked_returns_string(self):
        self.trip.budget = 100000
        self.trip.book_a_trip("Brazil")
        self.trip.book_a_trip("New Zealand")
        result = self.trip.booking_status()
        expected = """Booked Destination: Brazil
Paid Amount: 16740.00
Booked Destination: New Zealand
Paid Amount: 20250.00
Number of Travelers: 3
Budget Left: 63010.00"""

        self.assertEqual(expected, result)

if __name__ == "__main__":
    main()