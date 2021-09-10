from Person import Person
class Lecturer(Person):
    def __init__(self,name,nric,staff_id):
        super().__init__(name,nric)
        self.__staff_id = staff_id
        self.__total_TeachingHour = 1.5
        while True:
            try:
                self.__total_TeachingHour = int(input("Enter Total Teaching Hours: "))
            except ValueError:
                print("Invalid Input Type!")
            if self.__total_TeachingHour<0:
                print("Teaching Hours can't be less than 0!")
                continue
            if type(self.__total_TeachingHour)==int:
                break
    def computeSalary(self):
        salary = 90 * self.__total_TeachingHour
        return salary
    def __str__(self):
        return f"{self.get_name()}, Staff ID: {self.__staff_id} earns ${Lecturer.computeSalary(self):.2f}"
