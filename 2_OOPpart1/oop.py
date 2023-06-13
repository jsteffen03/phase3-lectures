# What is object oriented programming?
x = 3
x = "pigeon"


class Bird:
    name = None
    fly = False
    speed = None

    def printFly(self):
        print(f"{self.name} is {self.fly}")

bird = Bird()
bird2 = Bird()
bird.name = "pigeon"
# How do we expand it? What else does it contain? What else could it contain?
bird.fly = True
bird.speed = 10
bird2.name = "pigeon"
bird2.fly = False
bird2.speed = 10
print(bird, bird2)
bird2.printFly()
# What else do we want to do with this? Thinking about oop what functions can we create