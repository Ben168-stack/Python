from Person import Person
class Lecturer(Person):
    def __init__(self,name,nric,staff_id):
        super().__init__(name,nric)
        self.__staff_id = staff_id
    def computeSalary(self,total_TeachingHour):
        self.__total_TeachingHour = total_TeachingHour
        salary = 90 * self.__total_TeachingHour
        return salary
    def __str__(self):
        return f"{self.get_name()}, Staff ID: {self.get_nric()} earns ${}"
