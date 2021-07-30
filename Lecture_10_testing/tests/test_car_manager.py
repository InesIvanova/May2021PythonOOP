from Lecture_10_testing.car_manager import Car

from unittest import TestCase, main


class TestCar(TestCase):
    def setUp(self):
        self.car = Car(fuel_capacity=100, fuel_consumption=5.6, make="Test", model="TestModel")

    def test_init_creates_all_attributes(self):
        self.assertEqual(100, self.car.fuel_capacity)
        self.assertEqual(5.6, self.car.fuel_consumption)
        self.assertEqual(0, self.car.fuel_amount)
        self.assertEqual("Test", self.car.make)
        self.assertEqual("TestModel", self.car.model)

    def test_negative_fuel_capacity_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = -2
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_set_fuel(self):
        self.car.fuel_capacity = 20
        self.assertEqual(20, self.car.fuel_capacity)

    def test_empty_model_name_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_set_model(self):
        self.car.model = "New Model"
        self.assertEqual("New Model", self.car.model)

    def test_empty_make_name_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_set_make(self):
        self.car.make = "New Make"
        self.assertEqual("New Make", self.car.make)

    def test_negative_fuel_consuption_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = -2
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_set_consuption(self):
        self.car.fuel_consumption = 20
        self.assertEqual(20, self.car.fuel_consumption)

    def test_refuel_adds_fuel(self):
        self.assertEqual(0, self.car.fuel_amount)
        self.car.refuel(10)
        self.assertEqual(10, self.car.fuel_amount)

    def test_refuel_with_negative_raises(self):
        self.assertEqual(0, self.car.fuel_amount)
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-10)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_drive_without_fuel_raises(self):
        self.assertEqual(0, self.car.fuel_amount)
        with self.assertRaises(Exception) as ex:
            self.car.drive(10)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive(self):
        self.car.refuel(100)
        self.assertEqual(100, self.car.fuel_amount)
        self.car.drive(10)
        self.assertEqual(99.44, self.car.fuel_amount)

    def test_drive_with_not_enough_fuel_raises(self):
        self.car.refuel(0.1)
        with self.assertRaises(Exception) as ex:
            self.car.drive(10)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))


if __name__ == "__main__":
    main()