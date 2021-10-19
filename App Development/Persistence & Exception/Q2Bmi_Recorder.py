weight = ''
height = ''
while True:
    name = input("Enter name: ")
    while True:
        try:
            weight = float(input("Enter weight(KG): "))
            height = float(input("Enter height(M): "))
        except ValueError:
            print('Please enter a valid number!')
        if type(weight) == float and type(height) == float:
            break

    bmi = weight / height ** 2
    print(bmi)

    command = input("Store your bmi to file? (Y/N): ")
    if command.upper() == 'Y':
        bmi_File = open('bmi.txt', 'a')
        bmi_File.write(f"{name} {bmi} \n")
        bmi_File.close()

    command = input("Do you want to continue (Y/N): ")
    if command.upper() == 'N':
        break
command = input("Do you want to view your BMI record in the file (Y/N): ")
if command.upper() == 'Y':
    try:
        bmi_File = open('bmi.txt', 'r')
        contents = bmi_File.read()
        print(contents)
        bmi_File.close()
        print('End of program')
    except IOError:
        print('An error has occurred trying to read')
