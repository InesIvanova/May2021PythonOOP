class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'



import unittest


class WorkerTests(unittest.TestCase):
    def setUp(self):
        self.worker = Worker("Test", 100, 10)

    def test_init_worker_with_integer_value_for_name(self):
        worker = Worker(55, 100, 10)
        self.assertEqual(55, worker.name)

    def test_worker_is_initialised_correctly(self):
        # Assert
        self.assertEqual("Test", self.worker.name)
        self.assertEqual(100, self.worker.salary)
        self.assertEqual(10, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_worker_energy_increased_after_rest(self):
        # Arrange
        self.assertEqual(10, self.worker.energy)
        # Act
        self.worker.rest()
        # Assert
        self.assertEqual(11, self.worker.energy)

    def test_person_works_with_negative_energy_raises(self):
        # Arrange
        worker = Worker("Test", 100, 0)

        # act
        with self.assertRaises(Exception) as ex:
            worker.work()

        # assertion
        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_worker_money_is_increased_after_work(self):

        self.assertEqual(0, self.worker.money)

        # Act
        self.worker.work()

        # Assert
        self.assertEqual(100, self.worker.money)

    def test_worker_energy_is_decreased_after_work(self):
        self.assertEqual(10, self.worker.energy)

        # Act
        self.worker.work()

        # Assert
        self.assertEqual(9, self.worker.energy)

    def test_get_info(self):
        # Act
        actual_result = self.worker.get_info()
        expected_result = "Test has saved 0 money."

        # Assert

        self.assertEqual(expected_result, actual_result)

if __name__ == "__main__":
    unittest.main()


