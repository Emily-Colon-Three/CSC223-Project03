import unittest
from parking_ticket import ParkingTicket

# Creates a ticket full of placeholder information, with a single minute illegal. Tests that the fine will be $25 as intended.
class OneMinuteIllegalFine(unittest.TestCase):
    def test_fine(self):
        self.ticket = ParkingTicket("N/A", "N/A", "N/A", 0, 1, "N/A", 0)
        self.assertEqual(self.ticket.fine, 25)

# Same as previous test, except with 60 illegal minutes. Should still have fine of $25.
class SixtyMinuteIllegalFine(unittest.TestCase):
    def test_fine(self):
        self.ticket = ParkingTicket("N/A", "N/A", "N/A", 0, 60, "N/A", 0)
        self.assertEqual(self.ticket.fine, 25)

# Makes a ticket with 61 illegal minutes reported; the calculated fine should be $35 for exceeding first hour.
class SixtyOneMinuteIllegalFine(unittest.TestCase):
    def test_fine(self):
        self.ticket = ParkingTicket("N/A", "N/A", "N/A", 0, 61, "N/A", 0)
        self.assertEqual(self.ticket.fine, 35)

# Makes a ticket with a whole 120 illegal minutes. However, fine should still be $35 for two hours of illegal parking.
class OneHundredTwentyMinuteIllegalFine(unittest.TestCase):
    def test_fine(self):
        self.ticket = ParkingTicket("N/A", "N/A", "N/A", 0, 120, "N/A", 0)
        self.assertEqual(self.ticket.fine, 35)

# Creates ParkingTicket object with 121 illegal minutes; breaks third hour, fine must be $45.
class OneHundredTwentyOneMinuteIllegalFine(unittest.TestCase):
    def test_fine(self):
        self.ticket = ParkingTicket("N/A", "N/A", "N/A", 0, 121, "N/A", 0)
        self.assertEqual(self.ticket.fine, 45)

# Report testing

# Creates ParkingTicket with basic, identifiable data for all fields, then prints out a report. The contents are test for what they contain.
class BasicReportTicket(unittest.TestCase):
    def setUp(self):
        self.ticket = ParkingTicket("Make", "Model", "Color", 123, 60, "LastName", 890)

    def test_contents(self):
        self.assertTrue("Make" in str(self.ticket))
        self.assertTrue("Model" in str(self.ticket))
        self.assertTrue("Color" in str(self.ticket))

        self.assertTrue("60" in str(self.ticket))
        self.assertTrue("$25" in str(self.ticket))

        self.assertTrue("LastName" in str(self.ticket))
        self.assertTrue("890" in str(self.ticket))
