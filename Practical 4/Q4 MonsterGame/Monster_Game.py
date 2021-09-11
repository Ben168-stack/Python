# from Monster import Monster
from MonsterSubClass import FireMonster
from MonsterSubClass import WaterMonster
from MonsterSubClass import GrassMonster
import random


class MonsterGame:
    def __init__(self):
        self.choose_monster()
        self.generate_monster()
        while True:
            choice = input("Start Battle(type 'start' when ready): ").upper()
            if choice == 'START':
                break

        self.battle()

    def choose_monster(self):
        monster = ''
        while monster not in ['F', "W", "G"]:
            monster = input("Choose your monster (F, W or G): ").upper()
            if monster == 'F':
                self.player_monster = FireMonster()
                print(f"You Choose {self.player_monster._Monster__name}")
            elif monster == 'W':
                self.player_monster = WaterMonster()
                print(f"You Choose {self.player_monster._Monster__name}")
            elif monster == 'G':
                self.player_monster = GrassMonster()
                print(f"You Choose {self.player_monster._Monster__name}")
            else:
                print("Invalid Monster Type!")

    def generate_monster(self):
        monsters = [FireMonster(), WaterMonster(), GrassMonster()]
        random_num = random.randint(0, (len(monsters) - 1))
        self.computer_monster = monsters[random_num]
        print(f"Your Opponent Will be {self.computer_monster._Monster__name}")

    def battle(self):
        net_difference_playerAttack = (self.player_monster._Monster__attack) - (self.computer_monster._Monster__defence)
        net_difference_computerAttack = (self.computer_monster._Monster__attack) - (
            self.player_monster._Monster__defence)
        player_health = (self.player_monster._Monster__health)
        computer_health = (self.computer_monster._Monster__health)
        while True:
            print(
                f"Your {self.player_monster._Monster__name} dealt {net_difference_playerAttack} damage to {self.computer_monster._Monster__name} ,its health is now {computer_health}")
            computer_health -= net_difference_playerAttack
            if computer_health <= 0:
                print("You Won The Battle!")
                break
            player_health -= net_difference_computerAttack
            print(
                f"Your {self.player_monster._Monster__name} suffered {net_difference_computerAttack} damage to {self.computer_monster._Monster__name} ,your monster's health is now {player_health}")
            if player_health <= 0:
                print("You Lost The Battle!")
                break


MonsterGame()
# print(GrassMonster().__dict__)
# print(FireMonster().__dict__)
# print(WaterMonster().__dict__)
