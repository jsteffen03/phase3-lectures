class Animal:
    pass

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.food = 0
        self.love = 0
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.food = 0
        self.love = 0

# 1) Lets add an init that makes sense at Animal
# 2) Also lets add a universal method for all animals
# 3) Now we have to add Animal to be the parent of each class!
# 4) How do we use the keyphrase super()? We can use it to invoke a feature of the parent class
# 5) We can even use super().__init__()!