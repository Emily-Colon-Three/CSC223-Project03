class parking_meter:

    def __init__(self, purchased_time):
        self.purchased_time = purchased_time

    @property
    def purchased_time(self):
        return self.purchased_time

    @purchased_time.setter
    def purchased_time(self, new):
        if new >= 0:
            self.purchased_time = new
        else:
            raise ValueError("purchased_time must be >= 0")