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
        if type(player) is Player:
            self.players.append(player)
            if player.team:
                player.team.removePlayer(player)
            player.team = self
            player.history.append(self)

    def removePlayer(self,player_to_remove):
        for player in self.players:
            if player == player_to_remove:
                self.players.remove(player_to_remove)


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

class Player:
    def __init__(self,name,number):
        self.name = name
        self.number = number
        self.history = []
        self.team = None

if __name__ == '__main__':
    nuggets = NBATeams("Nuggets","Rocky")
    heats = NBATeams("Heats","Fury")
    jokic = Player("Jokic",15)
    nuggets.addPlayer(jokic)
    print(jokic.history)
    print(jokic.team.name)
    print(nuggets.players)
    heats.addPlayer(jokic)
    print(jokic.history)
    print(jokic.team.name)
    print(heats.players)
    print(nuggets.players)
    heats.removePlayer(jokic)
    print(heats.players)