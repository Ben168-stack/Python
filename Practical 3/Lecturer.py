from Person import Person
class Lecturer(Person):
    def __init__(self,name,nric,staff_id):
        super().__init__(name,nric)
        self.__staff_id = staff_id
        self.__total_TeachingHour = ''
        while type(self.__total_TeachingHour)!=int:
            try:
                self.__total_TeachingHour = int(input("Enter Total Teaching Hours: "))
            except ValueError:
                print("Invalid Input Type!")
    def computeSalary(self):
        salary = 90 * self.__total_TeachingHour
        return salary
    def __str__(self):
        return f"{self.get_name()}, Staff ID: {self.get_nric()} earns ${Lecturer.computeSalary(self):.2f}"
