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
        return f"The commission of salesperson {saleperson.get_name()} is ${saleperson.get_commission()}"


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
