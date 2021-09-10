from Monster import Monster


class FireMonster(Monster):
    def __init__(self, name='firebug', health=10, attack=9, defence=4):
        super().__init__(name, health, attack, defence)


class WaterMonster(Monster):
    def __init__(self, name='waterbird', health=15, attack=6, defence=3):
        super().__init__(name, health, attack, defence)


class GrassMonster(Monster):
    def __init__(self, name='grasshopper', health=20, attack=5, defence=3):
        super().__init__(name, health, attack, defence)
def display_info(monster):
    try:
        if monster._Monster__name == 'firebug':
            print(f"{monster._Monster__name} is a Fire Type monster")
        elif monster._Monster__name == 'waterbird':
            print(f'{monster._Monster__name} is a Water Type monster')
        elif monster._Monster__name == 'grasshopper':
            print(f"{monster._Monster__name} is a Grass Type monster")
        else:
            print("Invalid monster type")
    except:
        print("Invalid monster type")
m1 = FireMonster()
m2 = WaterMonster()
m3 = GrassMonster()

display_info(m1)
display_info(m2)
display_info(m3)
display_info('hi')
print(m2.__dict__) #very helpful yes stonks
