class ParkingMeter:
    """ParkingMeter is a very simple class with one property.
    purchased_time is an integer representing the number of minutes bought on the meter.
    number of minutes cannot be less than 0; in that case, ValueError is raised.
    It is inspected and passed into the PoliceOfficer class."""

    def __init__(self, purchased_time):
        self.minutes_purchased = purchased_time

    @property
    def minutes_purchased(self) -> int:
        return self._minutes_purchased

    @minutes_purchased.setter
    def minutes_purchased(self, new):
        if new >= 0:
            self._minutes_purchased = new
        else:
            raise ValueError("minutes_purchased must be >= 0")