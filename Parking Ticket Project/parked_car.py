class ParkedCar:
    """Represents a parked car, which has been parked somewhere for a variable amount of
    time, which is stored as a positive integer named minutes_parked.
    Includes getter and setter methods for the car's properties, which include the make,
    model, color, license plate number (license_number), and minutes_parked."""

    def __init__(self, make, model, color, license_number, minutes_parked):
        self.make = make
        self.model = model
        self.color = color
        self.license_number = license_number
        self.minutes_parked = minutes_parked

    @property
    def make(self) -> str:
        return self.make

    @make.setter
    def make(self, new):
        self.make = new

    @property
    def model(self) -> str:
        return self.model

    @model.setter
    def model(self, new):
        self.model = new

    @property
    def color(self) -> str:
        return self.color

    @color.setter
    def color(self, new):
        self.color = new

    @property
    def license_number(self) -> int:
        return self.license_number

    @license_number.setter
    def license_number(self, new):
        self.license_number = new

    @property
    def minutes_parked(self) -> int:
        return self.minutes_parked

    # Checks that the set value for minutes_parked is 0 or more, else ValueError raised
    @minutes_parked.setter
    def minutes_parked(self, new):
        if (new >= 0):
            self.minutes_parked = new
        else:
            raise ValueError("minutes_parked must be >= 0")