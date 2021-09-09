class Employee:
    def __init__(self,name,id,department,title):
        self.__name = name
        self.__id = id
        self.__department = department
        self.__title = title
    def __str__(self):
        return f'Name: {self.__name}, ID: {self.__id}, Department: {self.__department}, ' \
               f'Title: {self.__title}'
