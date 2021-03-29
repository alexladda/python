class Vehicle:
    # Class Attributes should not be changed
    vehicle_counter = 0

    # instructions how to initialize: constructor
    def __init__(self, body_type, make):
        self.vehicle_body = body_type
        self.vehicle_make = make
        Vehicle.vehicle_counter += 1

    def get_vehicle_count(self):
        # associate the Value with the class!
        return Vehicle.vehicle_counter



# each car object is an instance of the Vehicle class using instance Variables
car1 = Vehicle('jeep', 'toyota')
print(car1.get_vehicle_count())
car2 = Vehicle('truck', 'mercedes')
car3 = Vehicle('sedan', 'toyota')
print(car3.get_vehicle_count())
car4 = Vehicle('truck', 'mercedes')
car5 = Vehicle('motorcycle', 'mercedes')
car6 = Vehicle('sedan', 'honda')
print(car6.get_vehicle_count())

print(car1.get_vehicle_count())
print(car3.get_vehicle_count())
print(car6.get_vehicle_count())

print(car1.vehicle_make)
