# Lets take what we've done in one to many and allow it to be reversed!
class Bar:
    # Initialize the bar class that has Cocktails
    def __init__(self,name,location):
        self.name = name
        self.location = location
        self.cocktails = []
    def addCocktail(self, cocktail):
        self.cocktails.append(cocktail)
        cocktail.bars.append(self)

class Cocktail:
    def __init__(self,name,spirit):
        self.name = name
        self.spirit = spirit
        self.bars = []
    def __repr__(self):
        return f"Drink name: {self.name}"

if __name__ == '__main__':
    retroRoom = Bar("Retro Room","19th and Lawerence")
    oldFashion = Cocktail("Old Fashioned", "Whiskey")

    flatironHiddenBar = Bar("Flatiron Speakeasy", "Blake")
    cosmopoloten = Cocktail("Cosmopoloten", "Vodka")

    retroRoom.addCocktail(oldFashion)
    retroRoom.addCocktail(cosmopoloten)
    flatironHiddenBar.addCocktail(cosmopoloten)\
    
    print(retroRoom.cocktails)
    print(flatironHiddenBar.cocktails)
    print(oldFashion.bars)
    # First let us define a few bars and drinks

    # Now we attatch the drinks to the bars and vice versa
    # Now lets print out all of the bars that contain a certain drink
    # Also lets print all of the drinks in a bar
    pass

# To prepare for the future as we are thinking about sql how can we do many to many? one to many?
# We would need to think in ids!