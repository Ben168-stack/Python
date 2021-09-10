class Person:
    def __init__(self,name,nric):
        self.__name = name
        self.__nric = nric
    def get_nric(self):
        return self.__name
    def get_name(self):
        return self.__name
    def __str__(self):
        s = f'Name: {self.__name} NRIC: {self.__nric}'
        return s
