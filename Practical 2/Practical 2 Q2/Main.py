from Phone import Phone
from Owner import Owner

def valid_email(email):
    if '@' in email and email[-4:] == ".com":
        return True
    else:
        return False
def valid_phone_number(phone):
    if len(phone) ==8 and phone.isnumeric():
        return True
    else:
        print("Invalid Phone Number")
        return False

owner_name = input("Enter Owner Name: ")
while True:
    email_address = input("Enter Email Address: ")
    emailCheck = valid_email(email_address)
    if emailCheck == True:
        print(Owner(owner_name,email_address))
        break
    else:
        print("Invalid Email")
        continue

while True:
    phone = input("Enter Phone number: ")
    numberCheck = valid_phone_number(phone)
    if numberCheck == True:
        break
    else:
        continue

name = input("Enter Owner Name: ")
p = Phone(phone,name)
print(p)
