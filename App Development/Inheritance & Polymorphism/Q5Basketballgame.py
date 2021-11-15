class Player():
    def __init__(self,name):
        self.__name = name

    def set_name(self,name):
        self.__name = name
    def get_name(self):
        return self.__name

class BasketballPlayer(Player):
    valid_positions = ['Guard', 'Forward', 'Center']
    def __init__(self,name,position):
        self.__position = position
        super().__init__(name)
    def get_player_name(self):
        return self.get_name()
    def get_position(self):
        return self.__position

class BasketballGame():
    players = []
    count = 0
    team_name = input('Enter the Basketball Team:')
    while count != 5:
        name = input("Enter Player Name: ")
        position = input("Which position is he/she playing?: ").title()
        if position not in BasketballPlayer.valid_positions:
            print('Invalid Position')
            continue
        player = BasketballPlayer(name,position)
        players.append(player)
        count+=1
    print(f"{team_name} consist of the following players")
    for i in range(len(players)):
        print(f"{players[i].get_player_name()} playing as {players[i].get_position()}")
