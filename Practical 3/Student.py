from Person import Person
class Student(Person):
    final_MarkList = []
    def __init__(self,name,nric,admin_no):
        super().__init__(name,nric)
        self.__admin_no = admin_no
        self.__test_mark = ''
        self.__exam_mark = ''
        while True:
            try:
                self.__test_mark = int(input("Enter Test mark: "))
            except ValueError:
                print("Invalid Input Type!")
            if type(self.__test_mark)==int:
                break
            if self.__test_mark<0:
                print("Test Mark can't be less than 0!")
                continue
            elif self.__test_mark>100:
                print("Test Mark can't be less than 100!")
        while True:
            try:
                self.__exam_mark = int(input("Enter Exam mark: "))
            except ValueError:
                print("Invalid Input Type!")
            if type(self.__exam_mark)==int:
                break
            if self.__exam_mark<0:
                print("Exam Mark can't be less than 0!")
                continue
            elif self.__exam_mark>100:
                print("Exam Mark can't be more than 100!")
                continue

    def computeFinalMark(self):
        return (self.__exam_mark+self.__test_mark)/2
    def __str__(self):
        return f"{self.get_name()}, Admin No: {self.__admin_no} final mark is {Student.computeFinalMark(self):.2f}"

