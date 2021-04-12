class Vehicle:
    def __init__(self, body_type, make):         # instructions how to initialize: constructor
        self.vehicle_body = body_type
        self.vehicle_make = make


car1 = Vehicle('jeep', 'toyota')
car2 = Vehicle('truck', 'mercedes')
car3 = Vehicle('sedan', 'toyota')
car4 = Vehicle('truck', 'mercedes')
car5 = Vehicle('motorcycle', 'mercedes')
car6 = Vehicle('sedan', 'honda')


print(car1.vehicle_make)
print(type(car1))
print(car2.vehicle_make)
