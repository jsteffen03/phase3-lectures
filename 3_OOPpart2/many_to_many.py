# Lets take what we've done in one to many and allow it to be reversed!
class Bar:
    # Initialize the bar class that has Cocktails
    def __init__(self):
        pass

class Cocktail:
    def __init__(self,name,spirit):
        pass

if __name__ == '__main__':
    # First let us define a few bars and drinks

    # Now we attatch the drinks to the bars and vice versa
    # Now lets print out all of the bars that contain a certain drink
    # Also lets print all of the drinks in a bar
    pass

# To prepare for the future as we are thinking about sql how can we do many to many? one to many?
# We would need to think in ids!