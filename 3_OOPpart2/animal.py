class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species
    def pet(self):
        print("petting")
    def adopt(self):
        pass

class Cat(Animal):
    def __init__(self,name,species,color):
        super().__init__(name,species)
        self.color = color

class Dog(Animal):
    def __init__(self,name,species):
        super().__init__(name,species)
    def giveTreat(self):
        print("Giving treat")

class nestedDog(Dog):
    def __init__(self,name,species):
        super().__init__(name,species)


# 1) Lets add an init that makes sense at Animal
midna = Cat(name="Midna",species="Long Haired Tabby", color = "Black/white")
tracker = nestedDog(name="Tracker",species="Hound")
midna.pet()
tracker.giveTreat()
tracker.pet()
# 2) Also lets add a universal method for all animals
# 3) Now we have to add Animal to be the parent of each class!
# 4) How do we use the keyphrase super()? We can use it to invoke a feature of the parent class
# 5) We can even use super().__init__()!