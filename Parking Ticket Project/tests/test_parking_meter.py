import unittest

from parking_meter import ParkingMeter

# Constructs a ParkingMeter object, then tests that the minutes_purchased is correct. This validates both the value and that the object was created.
class ParkingMeterConstructor(unittest.TestCase):
    def setUp(self):
        self.meter = ParkingMeter(45)

    def test_meter(self):
        self.assertEqual(self.meter.minutes_purchased, 45)