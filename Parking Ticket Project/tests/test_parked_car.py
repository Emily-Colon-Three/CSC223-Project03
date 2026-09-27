import unittest

from parked_car import ParkedCar

# Creates a valid ParkedCar object, then tests all its properties.
class ValidParkedCar(unittest.TestCase):
    def setUp(self):
        self.car = ParkedCar("Ford", "F150", "Blue", 89052, 49)

    def test_parked_car(self):
        self.assertEqual(self.car.make, "Ford")
        self.assertEqual(self.car.model, "F150")
        self.assertEqual(self.car.color, "Blue")
        self.assertEqual(self.car.license_number, "89052")
        self.assertEqual(self.car.minutes_parked, 49)