# Practical 2 Part B Qn 2
class Owner:
    def __init__(self,name,email):
        self.__name = name
        self.__email = email
    def get_name(self):
        return self.__name
    def get_email(self):
        return self.__email
    def __str__(self):
        return f'Name: {self.__name}, Email: {self.__email}'
