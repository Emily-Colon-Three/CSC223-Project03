from police_officer import PoliceOfficer
from parked_car import ParkedCar
from parking_meter import ParkingMeter

# Main will mainly serve as a basic demonstration of the simulation and class interactions.

# Create objects
car1 = ParkedCar("Tesla", "Cybertruck", "Gray", 188, 45)
car2 = ParkedCar("Honda", "Oddysey", "Red", 199, 85)

meter1 = ParkingMeter(15)
meter2 = ParkingMeter(120)

officer = PoliceOfficer("Pickett", 985)

# Scenario 1: Violation
officer.inspect_vehicle(car1, meter1)

# Scenario 2: No Violation
officer.inspect_vehicle(car2, meter2)
