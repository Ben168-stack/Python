class Phone:
    def __init__(self,make,model,price):
        self.__make = make
        self.__model = model
        self.__price = price
        self.count = 0
    def get_make(self):
        return self.__make
    def get_model(self):
        return self.__model
    def get_price(self):
        return self.__price
    def edit_make(self,make):
        self.__make = make
    def edit_model(self,model):
        self.__model = model
    def edit_price(self,price):
        self.__price = price
    def __str__(self):
        self.count+=1
        return f"The price of {phone.get_make()} {phone.get_model()} is ${phone.get_price()}"
def addPhone(id,phone):
    phones[id] = phone
    print("Phone added Successfully!")
phones = {}
while True:
    print("Select the program (1-5) to run:")
    print("1. Search for a new phone")
    print("2. Add a new phone")
    print("3. Update phone details")
    print("4. Delete a phone")
    print("5. Quit the program")
    command = input("Enter your command (1-5): ")
    if command == "1":
        if len(phones) !=0:
            while True:
                print("Phone Directory:")
                for key in phones:
                    print(f"Phone ID: {key}: ")
                command2 = input("Please enter phone ID,EXIT(E) : ").upper().strip()
                if command2 == 'E':
                    break
                if command2 in phones:
                    print(phones[command2])
        else:
            print("No phones recorded yet!")
    if command == "2":
        id = input('Enter ID of Phone: ').strip().upper()
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
        addPhone(id,phone)
    if command == '3':
        while True:
            print("Phone Directory:")
            for key in phones:
                print(f"Phone ID: {key}: ")
            command2 = input("Enter ID of phone to be changed,EXIT(E): ").upper().strip()
            if command2 in phones:
                while True:
                    current_phone = phones[command2]
                    print(current_phone)
                    attribute = input('Enter attribute to change(ID,MAKE,MODEL,PRICE), EXIT(E): ').upper().strip()
                    if attribute == 'E':
                        break
                    elif attribute == 'MAKE':
                        new_attribute = input("Enter New Make: ")
                        phones[command2].edit_make(new_attribute)
                        print('Make attribute changed successfully!')
                    elif attribute == 'MODEL':
                        new_attribute = input("Enter New Model: ")
                        phones[command2].edit_model(new_attribute)
                        print('Model attribute changed successfully!')
                    elif attribute == 'PRICE':
                        new_attribute = input("Enter New Price: ")
                        phones[command2].edit_price(new_attribute)
                        print('Price attribute changed successfully!')
                    elif attribute == "ID":
                        new_attribute = input("Enter New ID: ").upper().strip()
                        phones[new_attribute] = phones.pop(command2)
                        break

    if command == '4':
        while True:
            print("Phone Directory:")
            for key in phones:
                print(f"Phone ID: {key}: ")
            command2 = input("Enter ID of phone to be deleted,EXIT(E): ").upper().strip()
            if command2 in phones:
                del phones[command2]
                print("Phone Removed Successfully!")
            elif command2 == 'E':
                break



    if command == '5':
        print("Goodbye!")
        exit()


