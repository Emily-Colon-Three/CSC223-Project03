class ParkedCar:
    """Represents a parked car, which has been parked somewhere for a variable amount of
    time, which is stored as a positive integer named minutes_parked.
    Includes getter and setter methods for the car's properties, which include the make,
    model, color, license plate number (license_number), and minutes_parked."""

    def __init__(self, make: str, model: str, color: str, license_number: int, minutes_parked: int):
        self.make = make
        self.model = model
        self.color = color
        self.license_number = license_number
        self.minutes_parked = minutes_parked

    @property
    def make(self) -> str:
        return self._make

    @make.setter
    def make(self, new):
        self._make = new

    @property
    def model(self) -> str:
        return self._model

    @model.setter
    def model(self, new):
        self._model = new

    @property
    def color(self) -> str:
        return self._color

    @color.setter
    def color(self, new):
        self._color = new

    @property
    def license_number(self) -> int:
        return self._license_number

    @license_number.setter
    def license_number(self, new):
        self._license_number = new

    @property
    def minutes_parked(self) -> int:
        return self._minutes_parked

    # Checks that the set value for minutes_parked is 0 or more, else ValueError raised
    @minutes_parked.setter
    def minutes_parked(self, new):
        if (new >= 0):
            self._minutes_parked = new
        else:
            raise ValueError("minutes_parked must be >= 0")