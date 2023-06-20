
class Pet:
    def __init__(self,name,species):
        self.name = name
        self.species = species
        self.owner = None
        pass

class Owner:
    def __init__(self,name):
        self.name = name
        self.pet = None

    def adopt(self,pet):
        if type(pet) is Pet:
            self.pet = pet
            pet.owner = self
        else:
            raise Exception("Not valid pet")



if __name__ == '__main__':
    midna = Pet(name = "Midna",species = "Long Haired Tabby")
    david = Owner(name = "David")
    david.adopt("midna")

    print(midna.owner.name)
    pass