from parking_ticket import ParkingTicket

class PoliceOfficer:
    """PoliceOfficer is a class which acts upon the data of ParkedCar and ParkingMeter objects,
    while creating a ParkingTicket object if a violation is detected. While it carries out the
    violation detection and minutes over calculation, ParkingTicket handles fine calculation.
    Also prints out the ParkingTicket object's report after a violation before returning it.
    Has two properties, officer name and officer badge number (badge_num). The former is a string,
    the latter an int. They have getter and setter methods, and are used in the inspect_vehicle
    method."""

    def __init__(self, name, badge_num):
        self.name = name
        self.badge_num = badge_num

    @property
    def name(self) -> str:
        return self._name
    @name.setter
    def name(self, new):
        self._name = new

    @property
    def badge_num(self) -> int:
        return self._badge_num
    @badge_num.setter
    def badge_num(self, new):
        self._badge_num = new

    # A method which takes a Parkedcar and ParkingMeter object as parameters, comparing the minutes parked on the car to
    # the purchased amount on the meter. If the car is parked illegally and a violation is found, a ParkingTicket object
    # will be created and returned with necessary info. If no violation is found, None is returned.
    def inspect_vehicle(self, ParkedCar, ParkingMeter) -> ParkingTicket | None:
        minutes_over = ParkedCar.minutes_parked - ParkingMeter.minutes_purchased

        if minutes_over > 0:
            self.officer_ticket = ParkingTicket(ParkedCar.make, ParkedCar.model, ParkedCar.license_number, minutes_over, self._name, self._badge_num)

            print(str(self.officer_ticket)) # Print out ticket report to terminal
            return self.officer_ticket
        else:
            return None