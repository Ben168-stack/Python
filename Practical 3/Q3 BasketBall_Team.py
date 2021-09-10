class Player:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


class BasketballPlayer(Player):
    # players = []
    def __init__(self, name, position):
        super().__init__(name)
        self.__position = position
    def get_position(self):
        return self.__position
    # def create_player(self):
    #     self.players.append(BasketballPlayer(super().get_name(), self.__position))

def valid_position(position):
    valid_positions = ['Guard', 'Forward', 'Center']
    if position not in valid_positions:
        return False
    else:
        return True
team_name = input("Enter the basketball team name: ")
count = 0
players = []
while count!=5:
    name = input("Enter player name: ").title()
    while True:
        position = input("Which position is he/she playing? ").title()
        positionCheck = valid_position(position)
        if positionCheck == True:
            break
        else:
            print("Invalid Position!")
    p = BasketballPlayer(name,position)
    players.append(p)
    count+=1
print(f"Team {team_name} consist of the following players: ")
for i in range(len(players)):
    player = players[i].get_name()
    position = players[i].get_position()
    print(f"{player} playing as a {position}")

