# 1) Lets create a class, use pass and create a class! Then use 
#    __init__ think of the key attributes of it
print('hello')
class Cat:
    # Global class variables
    all_cats = []
    unique_species = []
    valid_colors = ["black","white","brown"]
    # Init, runs on creating this class
    def __init__(self,species,name="No name",color = "orange"):
        self._name = name
        self.species = species
        self.time_called = 0
        if color in Cat.valid_colors:
            self.color = color
        else:
            raise Exception("Not valid color")
        Cat.all_cats.append(self)
        if species not in Cat.unique_species:
            Cat.unique_species.append(species)
    # Methods!
    # Properties
    # Takes inputs, functions
    def get_name(self):
        self.time_called += 1
        print(f"Called {self._name} {self.time_called} times")
        return self._name
    def set_name(self, value):
        if value:
            self._name = value
    name = property(get_name,set_name)
    # Orders matters, check documentation linked below!
    def pet(self):
        from exportexample import new_cat
        print("meow happily")
    # Class Methods!
    @classmethod
    def pet_all(cls):
        for cat in cls.all_cats:
            print(f"Petting {cat.name}")
    

    def __repr__(self):
        return f"Name: {self.name}, species: {self.species}"

    # This runs when we run print on the class
midna = Cat(name = "Midna",species="Longhair", color="anjipdsbnhgae")
if __name__ == "__main__":
    # 2) Now lets instantiate a few of them. A question is, are they the same?
    
    # print(midna.unique_species)
    chanel = Cat(name = "Chanel",species="Tabby", color="brown")
    # print(midna.unique_species)
    # new_cat = Cat(name = "Bob",species="Longhair", color="black")
    # print(new_cat.unique_species)
    midna.color = "Not valid color"
    midna.pet_all()
    # midna.name
    # midna.name = ""
    # midna.name
    # midna.name
    # midna.name
    # for cat in Cat.all_cats:
    #     print(cat.species)
    # 3) Global Class variables???
    # 4) Using self
    # 5) Creating a method for this class
    # 6) Using __repr__
    # 7) Using Properties, property(), to set setters and getter functions (https://www.programiz.com/python-programming/property)
    # 8) Decorators and CLS (@classmethod)
    pass