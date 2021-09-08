# Part A Practical 2 Qn 2
class Phone:
    count = 0
    def __init__(self,number,owner):
        self.__number = number
        self.__owner = owner
        self.__class__.count +=1
    def get_number(self):
        return self.__number
    def get_owner(self):
        return self.__owner
    def __str__(self):
        return f'Name: {self.__owner}, Phone Number: {self.__number}'

