from Person import Person
class Lecturer(Person):
    def __init__(self,name,nric,staff_Id):
        super().__init__(name,nric)
        self.__staff_Id = staff_Id
        self.__total_TeachingHour = 0
    def set_staff_id(self,staff_id):
        self.__staff_Id = staff_id

    def set_total_TeachingHour(self, total_TeachingHour):
        self.__total_TeachingHour = total_TeachingHour

    def get_staff_id(self):
        return self.__staff_Id

    def get_total_TeachingHour(self):
        return self.__total_TeachingHour

    def computeSalary(self):
        return self.get_total_TeachingHour() * 90
    def __str__(self):
        return f"{self.get_name()}, staff id: {self.get_staff_id()} earns ${self.computeSalary()}"
