class Engine:
    all = []
    def __init__(self,id,name,cylinders,horsepower,car_id):
        self.id = id
        self.name = name
        self.cylinders = cylinders
        self.horsepower = horsepower
        Engine.all.append(self)
        for engine in Engine.all:
            if car_id == engine.car_id:
                raise Exception("Needs to be unique")
        self.car_id = car_id
class Car:
    def __init__(self,id,make,model,engine_id=None):
        self.id = id
        self.make = make
        self.model = model
        # self.engine_id = engine_id
        self.owner = None

# How do we connect the two?
class Tenent:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age
        self.leases = []

class Apartmant:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age
        self.leases = []
    def addTenent(self,price,unit_num,tenent):
        newLease = Lease(price,unit_num,tenent.id,self.id)
        self.leases.append(newLease)
        tenent.leases.append(newLease)

class Lease:
    def __init__(self,price,unit_num, tenent_id, apartment_id):
        self.price = price
        self.unit_num = unit_num
        self.tenent_id = tenent_id
        self.apartment_id = apartment_id