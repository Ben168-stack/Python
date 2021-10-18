class Customer:
    def __init__(self):
        self.__name = None
        self.__email = None
        self.__mobile_number = None

    def set_name(self,name):
        self.__name = name

    def set__email(self,email):
        self.__email = email

    def set__mobile_number(self,mobile_number):
        self.__mobile_number = mobile_number

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_mobile_number(self):
        return self.__mobile_number


name = input("Enter your name: ")
email = input("Enter your email: ")
while True:
    try:
        mobile_number = int(input('Enter your mobile number: '))
    except ValueError:
        print('Invalid Input')
        continue
    if len(str(mobile_number)) == 8 and type(mobile_number) == int:
        break
Customer = Customer()
Customer.set_name(name)
Customer.set__email(email)
Customer.set__mobile_number(mobile_number)
print(f"Name: {Customer.get_name()}")
print(f"Email: {Customer.get_email()}")
print(f"Mobile Number: {Customer.get_mobile_number()}")
