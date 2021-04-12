from machines.vehicle_stuff import Vehicle, Truck, Motorcycle


car1 = Vehicle('sedan', 'chevy')
truck1 = Truck('small rig', 'mercedes')
moto1 = Motorcycle('sports', 'honda')

for v in [truck1, car1, moto1]:
    v.drive() # polymorphism. this function could be vastly different

def perform_task(vehicle_object):
    vehicle_object.drive()

for v in [truck1, car1, moto1]:
    perform_task(v)
