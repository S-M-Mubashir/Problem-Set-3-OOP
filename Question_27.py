class PhysicalObject:
    def __init__(self):
        super().__init__()
        print("Physical Object")

class Vehicle(PhysicalObject):
    def __init__(self):
        super().__init__()
        print("Vehicle")

class GroundVehicle(Vehicle):
    def __init__(self):
        super().__init__()
        print("Ground Vehicle")

class FlyingVehicle(Vehicle):
    def __init__(self):
        super().__init__()
        print("Flying Vehicle")

class FuelTruck(GroundVehicle):
    def __init__(self):
        super().__init__()
        print("Fuel Truck")
    
class AirCraft(GroundVehicle,FlyingVehicle):
    def __init__(self):
        super().__init__()
        print("AirCraft")
 
class CommercialAirCraft(AirCraft):
    def __init__(self):
        super().__init__()
        print("Commercial AirCraft")

class Boeing707(CommercialAirCraft):
    def __init__(self):
        super().__init__()
        print("Boeing 707")



# Output will be reverse of the answers in Question_26 because
# here super is called first, instead of the print function of the class whose object is made
B = Boeing707()
print("-"*50)

A = AirCraft()
print("-"*50)

F = FuelTruck()
print("-"*50)

GV= GroundVehicle()
print("-"*50)

FV = FlyingVehicle()
print("-"*50)

V = Vehicle()
print("-"*50)
