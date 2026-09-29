import math

class ParkingTicket:
    """ParkingTicket represents a parking ticket, given all the data which it eventually reports
    upon construction. ParkedCar and PoliceOfficer data is copied, not referenced.
    Properties include car_make, car_model, and car_license, all pertaining to a reported car.
    illegal_minutes is the number of minutes car was reported over purchased time, validated so
    that it always is a positive integer. Passed in by PoliceOfficer.
    Remaining properties, officer_name and officer_badge, are copied from PoliceOfficer object.
    The ParkingTicket class automatically calculates fine amounts depending on number of illegal
    minutes stored, with $25 charged for the first hour and $10 for each subsequent hour.
    Includes __str__() dunder method, making it compatible with str() using custom behavior
    to output a readable report of all the data within the object."""

    def __init__(self, car_make, car_model, car_color, car_license, illegal_minutes, officer_name, officer_badge):
        self.car_make = car_make
        self.car_model = car_model
        self.car_color = car_color
        self.car_license = car_license
        self.illegal_minutes = illegal_minutes
        self.officer_name = officer_name
        self.officer_badge = officer_badge

        self.fine = self.calculate_fine(self.illegal_minutes)

    # Class Properties (getters and setters)

    @property
    def car_make(self) -> str:
        return self._car_make
    @car_make.setter
    def car_make(self, new):
        self._car_make = new

    @property
    def car_model(self) -> str:
        return self._car_model
    @car_model.setter
    def car_model(self, new):
        self._car_model = new

    @property
    def car_color(self) -> str:
        return self._car_color
    @car_color.setter
    def car_color(self, new):
        self._car_color = new

    @property
    def car_license(self) -> int:
        return self._car_license
    @car_license.setter
    def car_license(self, new):
        self._car_license = new

    @property
    def illegal_minutes(self) -> int:
        return self._illegal_minutes
    @illegal_minutes.setter
    def illegal_minutes(self, new):
        if (new <= 0):
            raise ValueError("illegal_minutes must be positive integer.")
        self._illegal_minutes = new

    @property
    def officer_name(self) -> str:
        return self._officer_name
    @officer_name.setter
    def officer_name(self, new):
        self._officer_name = new

    @property
    def officer_badge(self) -> int:
        return self._officer_badge
    @officer_badge.setter
    def officer_badge(self, new):
        self._officer_badge = new

    # Class Methods

    # Takes a count of illegal minutes as input, then outputs the resulting fine. The first hour is $25, every additional hour costs $10.
    def calculate_fine(self, illegal_minutes) -> int:
        illegal_hours = math.ceil(illegal_minutes / 60)
        fine = (illegal_hours - 1) * 10 + 25
        return fine

    # Returns a string when using str() for ParkingTicket which produces a full report of its contents.
    def __str__(self):
        return (
            # Car Data
            f"Car Make  : {self.car_make}\n"
            f"Car Model : {self.car_model}\n"
            f"Car Color : {self.car_color}\n"
            f"License # : {self.car_license}\n\n"
            
            # Citation and Fine
            f"Minutes Over Paid Limit   : {self.illegal_minutes}\n"
            f"Fine Amount               : ${self.fine}\n\n"
            
            # Issuing Officer Info
            f"Officer Name      : {self.officer_name}\n"
            f"Officer Badge #   : {self.officer_badge}"
        )
