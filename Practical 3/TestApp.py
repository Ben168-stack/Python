from Lecturer import Lecturer
from Student import Student
def is_valid_nric(s):
    if len(s) == 9:
        if s[0].upper() in ['S', 'T'] and s[-1].isalpha():
            for number in s[1:7]:
                if not number.isnumeric():
                    return False
            return True
    else:
        return False
def is_valid_admin_no(string):
    if len(string)==7:
        if string[:-1].isdigit():
            if string[-1].isalpha():
                return True
    return False
Lecturer_name = input("Enter Lecturer Name: ").title()

while True:
    Lecturer_NRIC = input("Enter Lecturer NRIC: ").upper()
    nric_check = is_valid_nric(Lecturer_NRIC)
    if nric_check == True:
        break
    else:
        print("Invalid NRIC!")
while True:
    Lecturer_ID = input("Enter Staff ID: ").upper()
    if Lecturer_ID!=Lecturer_NRIC:
        print("ID is not same as NRIC!")
        continue
    id_check = is_valid_nric(Lecturer_ID)
    if id_check == True:
        break
    else:
        print("Invalid ID!")

print(Lecturer(Lecturer_name,Lecturer_NRIC,Lecturer_ID))
student_name = input("Enter Student Name: ").title()
while True:
    student_nric = input("Enter Student NRIC: ").upper()
    nric_check = is_valid_nric(student_nric)
    if nric_check == True:
        break
    else:
        print('Invalid NRIC!')
while True:
    student_adminNo = input("Enter Student Admin No: ").upper()
    adminNo_check = is_valid_admin_no(student_adminNo)
    if adminNo_check == True:
        break
    else:
        print("Invalid Admin Number!")
print(Student(student_name,student_nric,student_adminNo))




