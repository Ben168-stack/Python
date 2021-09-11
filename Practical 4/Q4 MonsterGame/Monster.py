class Monster:
    def __init__(self,name,health,attack,defence):
        self.__name = name
        self.__health = health
        self.__attack = attack
        self.__defence = defence
    def __str__(self):
         return f"{self.__name} is a monster"
