import unittest

from parking_ticket import ParkingTicket
from police_officer import PoliceOfficer
from parked_car import ParkedCar
from parking_meter import ParkingMeter

# Creates a car and meter, the former of which has been parked for 15 of the 60 purchased minutes. Lets PoliceOfficer object inspect it; should return None.
class InspectUnderTime(unittest.TestCase):
    def setUp(self):
        self.car = ParkedCar("Toyota", "RAV4", "White", 99, 15)
        self.meter = ParkingMeter(60)
        self.officer= PoliceOfficer("Smith", 456)

    def test_no_violation(self):
        self.assertIsNone(self.officer.inspect_vehicle(self.car, self.meter))

# Creates a car parked for 60 of the 60 minutes purchased on a meter, officer inspects and should return none still.
class InspectAtTime(unittest.TestCase):
    def setUp(self):
        self.car = ParkedCar("Toyota", "RAV4", "White", 99, 60)
        self.meter = ParkingMeter(60)
        self.officer= PoliceOfficer("Smith", 456)

    def test_no_violation(self):
        self.assertIsNone(self.officer.inspect_vehicle(self.car, self.meter))

# Collaboration with ParkingTicket

# Creates a car parked over the meter limit by a whole hour, and has officer inspect it. Checks that the ticket has all the right information.
class CarAndOfficerInfoTicket(unittest.TestCase):
    def setUp(self):
        self.car = ParkedCar("Volkswagen", "Beetle", "Yellow", 6460, 120)
        self.meter = ParkingMeter(60)
        self.officer = PoliceOfficer("Jones", 234)
        self.ticket = self.officer.inspect_vehicle(self.car, self.meter)

    def test_ticket_car(self):
        self.assertEqual(self.ticket.car_make, "Volkswagen")
        self.assertEqual(self.ticket.car_model, "Beetle")
        self.assertEqual(self.ticket.car_color, "Yellow")
        self.assertEqual(self.ticket.car_license, 6460)

    def test_ticket_officer(self):
        self.assertEqual(self.ticket.officer_name, "Jones")
        self.assertEqual(self.ticket.officer_badge, 234)