# One to One
    # Review how to change relationships dynamically
class Engine:
    def __init__(self,name,cylinders,horsepower):
        self.name = name
        self.cylinders = cylinders
        self.horsepower = horsepower
        self.car = None
class Car:
    def __init__(self,make,model,engine=None):
        self.make = make
        self.model = model
        self.engine = engine
        self.owner = None

engine = Engine("E1","4 Cylinders", "10")
honda = Car("Honda", "Civic",engine)
engine.car = honda
print(engine.car.engine.car.engine)

# One to Many
class Owner:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.cars = []
        self.plants = []
    def buyCar(self,car):
        self.cars.append(car)
        car.owner = self
    def buyPlant(self,plant):
        self.plants.append(plant)
        plant.owners.append(self)

david = Owner("David","26")
david.buyCar(honda)
print(david.cars[0].make)
print(honda.owner.name)
# Many to Many
class Plant:
    def __init__(self,name,species,watered):
        self.name = name
        self.species = species
        self.watered = watered
        self.owners = []

# isinstance() supports inheritence! Type does not

class Flower(Plant):
    def __init__(self,name,species,watered):
        super().__init__(name,species,watered)

rose = Flower("Rose","Rosa Rubiginosa",True)
david.buyPlant(rose)
# print(type(rose) is Flower)
print(isinstance(rose,Plant))
print(type(rose) is Plant)