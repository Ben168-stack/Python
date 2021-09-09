from Employee import Employee

employees = {

}


def add_employee(id, employee):
    employees[id] = employee


# def update_employee_details(name,id,department,title):

command1 = ''
while True:
    while True:
        print("Select the program 1-5 to run:")
        print("1. Search for an employee")
        print("2. Add new employee")
        print("3. Update employee details")
        print("4. Delete an employee")
        print("5. Quit the program")
        choice = input("Enter your command (1-5): ")
        if choice == '1':
            while True:
                print("Employee Database:")
                for key in employees:
                    print(f"Employee ID: {key}")
                command = input("Find Employee(enter id)\nExit(E)\nEnter Choice: ").upper()
                if command in ["E", 'EXIT']:
                    break
                elif command not in employees:
                    print("Employee ID does not exist!")
                    continue
                elif command in employees:
                    while command1 not in ['E', "EXIT"]:
                        print(employees[command])
                        print("Exit(E)")
                        command1 = input("Enter Choice: ").upper()


        elif choice == '2':
            while True:
                name = input("Enter Employee's name: ").title()
                while True:
                    id = input("Enter Employee's ID: ").upper()
                    if id in ["EXIT", 'E']:
                        print("Illegal keywords")
                    else:
                        break
                department = input("Enter Employee's Department: ").title()
                title = input("Enter Employee's title: ").title()
                e = Employee(name, id, department, title)
                add_employee(id, e)
                print("Employee Added Successfully!")
                break
        elif choice == '3':
            while True:
                print("Employee Database:")
                for key in employees:
                    print(f"Employee ID: {key}")
                command = input("Enter Employee's ID to update, Exit(E)\nEnter Choice: ").upper()
                if command in ['EXIT', 'E']:
                    break
                elif command in employees:
                    while command1 not in ['E', "EXIT"]:
                        print(employees[command])
                        print("Exit(E)")
                        command1 = input("Enter attribute to change(Name,ID,Department,Title): ").upper()
                        if command1 == 'NAME':
                            name = input("Please enter new name: ").title()
                            employees[command].edit_name(name)
                            print("Name Changed Successfully!")
                        elif command1 == 'ID':
                            while True:
                                id = input("Enter Employee's ID: ").upper()
                                if id in ["EXIT", 'E']:
                                    print("Illegal keywords")
                                else:
                                    break
                            employees[command].edit_id(id)
                            print("ID Changed Successfully!")
                        elif command1 == "DEPARTMENT":
                            department = input("Please enter new Department: ").title()
                            employees[command].edit_department(department)
                            print("Department Changed Successfully!")
                        elif command1 == 'TITLE':
                            title = input("Please enter new title: ").title()
                            employees[command].edit_title(title)
                            print("Title Changed Successfully!")
                        elif command1 in ["EXIT", "E"]:
                            break
                        else:
                            print("Invalid Command!")


                elif command not in employees:
                    print('Employee ID does not exist')
                else:
                    print("Invalid Command!")

        elif choice == '4':
            while True:
                print("Employee Database:")
                for key in employees:
                    print(f"Employee ID: {key}")
                command = input("Enter Employee's ID to delete, Exit(E)\nEnter Choice: ").upper()
                if command in ['EXIT', "E"]:
                    break
                elif command in employees:
                    del (employees[command])
                    print("Employee Deleted Successfully")
                elif command not in employees:
                    print('Employee ID does not exist')
                else:
                    print("Invalid Command!")


        elif choice == '5':
            print("Goodbye.")
            exit()
        else:
            print("Invalid Command!")
