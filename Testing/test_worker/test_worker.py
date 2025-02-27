from unittest import TestCase, main
from Task_1.worker import Worker


class TestWorker(TestCase):

    # runs before each test case
    def setUp(self):
        self.worker = Worker(
            "TestGuy",
            25_000,
            100
        )

    def test_correct_init(self):
        self.assertEqual("TestGuy", self.worker.name)
        self.assertEqual(25_000, self.worker.salary)
        self.assertEqual(100, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_work_when_worker_has_energy_expect_money_increase_and_energy_decrease(self):
        expected_money = self.worker.salary * 2
        expected_energy = self.worker.energy - 2

        self.worker.work()
        self.worker.work()

        self.assertEqual(expected_money, self.worker.money)
        self.assertEqual(expected_energy, self.worker.energy)

    def test_work_when_worker_does_not_have_energy_raises_exception(self):
        self.worker.energy = 0 # Arrange

        with self.assertRaises(Exception) as ex: # Act
            self.worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))


    def test_rest_increases_energy_with_one(self):
        expected_energy = self.worker.energy + 1
        self.worker.rest()
        self.assertEqual(expected_energy, self.worker.energy)

    def test_get_info_returns_correct_string(self):
        expected_string = f'TestGuy has saved 0 money.'
        self.assertEqual(expected_string, self.worker.get_info())

if __name__ == "__main__":
    main()