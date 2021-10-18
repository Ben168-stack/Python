class Phone:
    def __init__(self,make,model,price):
        self.__make = make
        self.__model = model
        self.__price = price

    def __str__(self):
        return f"The price of {self.__make} {self.__model} is ${self.__price}"

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
print(Phone(make,model,price))
