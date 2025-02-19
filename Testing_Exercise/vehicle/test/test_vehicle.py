from unittest import TestCase, main
from project.vehicle import Vehicle


class TestVehicle(TestCase):

    def setUp(self):
        self.vehicle = Vehicle(100, 100)

    def test_default_fuel_consumption_is_correct_value(self):
        self.assertEqual(1.25, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_correct_init(self):
        self.assertEqual(100, self.vehicle.fuel)
        self.assertEqual(100, self.vehicle.capacity)
        self.assertEqual(100, self.vehicle.horse_power)
        self.assertEqual(self.vehicle.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_drive_when_not_enough_fuel_raises_exception(self):
        self.vehicle.fuel = 0

        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_with_enough_fuel_decreases_fuel(self):
        self.vehicle.drive(50)
        self.assertEqual(37.5, self.vehicle.fuel)

    def test_refuel_too_much_fuel_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(10000)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_with_less_fuel_adds_fuel(self):
        self.vehicle.fuel = 50
        self.vehicle.refuel(30)

        self.assertEqual(80, self.vehicle.fuel)

    def test_correct__str__method(self):
        expected_result = f"The vehicle has 100 " \
                          f"horse power with 100 fuel left and 1.25 fuel consumption"

        self.assertEqual(expected_result, str(self.vehicle))









if __name__ == "__main__":
    main()