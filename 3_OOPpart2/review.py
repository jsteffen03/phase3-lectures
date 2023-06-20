#!/usr/bin/env python3
# Create a class
class NBATeams:
    # Global variables for a class
    all_teams = []
    def __init__(self,name,mascot):
        self.name = name
        self.mascot = mascot
        self.players = []
        NBATeams.all_teams.append(self)
    # Create a method
    def addPlayer(self,player):
        self.players.append(player)

    def get_name(self):
        return self._name
    def set_name(self,value):
        if value:
            self._name = value
        else:
            raise Exception("Not valid name")
    name = property(get_name,set_name)

    @classmethod
    def callAllPlayers(cls):
        for team in cls.all_teams:
            for player in team.players:
                print(player)
        pass

    @staticmethod
    def staticPrint():
        print("Static")
    # def __str__(self):
    #     return f"{self.name}"

    # def __repr__(self):
    #     return f"{self.name} 1"



nuggets = NBATeams("Nuggets","Rocky")
heats = NBATeams("Heats","Fury")
print(NBATeams.all_teams[0].mascot)
nuggets.addPlayer("Jokic")
heats.addPlayer("Jimmy Butler")
heats.addPlayer("Florida Man")
# Properties, we can do any checks in here!!
# Decorators

def callOtherMethod(method):
    print("In call")
    method()
    method()

@callOtherMethod
def printHi():
    print("hello")

NBATeams.callAllPlayers()

nuggets.staticPrint()
# Review property underscore
# repr vs str

# Static methods
# - Do not require any instances so we don't need to pass self or cls