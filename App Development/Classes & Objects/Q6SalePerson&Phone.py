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
    count = 0

    def __init__(self, make, model, price):
        self.__make = make
        self.__model = model
        self.__price = price

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_price(self):
        return self.__price

    def __str__(self):
        self.count += 1
        return f"The phone created is {self.__make} {self.__model} priced at ${self.__price}. Now has {self.count} phone in total."


class SalesPerson:
    def __init__(self):
        self.__name = None
        self.__commission = None

    def set_name(self, name):
        self.__name = name

    def set_commission(self, commission):
        self.__commission = commission

    def get_name(self):
        return self.__name

    def get_commission(self):
        return self.__commission

    def __str__(self):
        return f"Salesperson {saleperson.get_name()} sold {phone.get_make()} {phone.get_model()} at ${phone.get_price()} and earned a commission of ${saleperson.get_commission()}"


make = input("Enter the make of the phone: ")
model = input("Enter the model of the phone: ")
while True:
    try:
        price = float(input("Enter the price of the phone: "))
    except ValueError:
        print("Invalid Value")
        continue
    if type(price) == float:
        break
phone = Phone(make, model, price)
print(Phone.__str__(phone))

name = input("Enter Sales Person's Name: ")

while True:
    payment = input(f"Enter Payment received by {name}: ")

    if payment.isnumeric():
        break
    else:
        print(bcolors.FAIL + "Payment should be in numbers!" + bcolors.ENDC)
        continue

commission = float(payment) * 0.02
saleperson = SalesPerson()
saleperson.set_name(name)
saleperson.set_commission(commission)
print(SalesPerson())
