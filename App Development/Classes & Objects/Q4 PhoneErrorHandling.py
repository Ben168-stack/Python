class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Phone:
    def __init__(self):
        self.__make = None
        self.__model = None
        self.__price = 0

    def set_make(self,make):
        self.__make = make

    def set_model(self,model):
        self.__model = model

    def set_price(self,price):
        self.__price = price

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_price(self):
        return self.__price

    def __str__(self):
        return f"The price of {phone.get_make()} {phone.get_model()} is ${phone.get_price()}"

phone = Phone()
make = input("Enter the make of the phone: ")
model = input("Enter the model of the phone: ")

while True:
    price = input("Enter the price of the phone: ")

    if price.isnumeric():
        break
    else:
        print(bcolors.FAIL + "Price should be in numbers" + bcolors.ENDC)
        continue
phone.set_make(make)
phone.set_model(model)
phone.set_price(price)
print(Phone())
print()
