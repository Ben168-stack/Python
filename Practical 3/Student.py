from Person import Person
class Student(Person):
    final_MarkList = []
    def __init__(self,name,nric,admin_no):
        super().__init__(name,nric)
        self.__admin_no = admin_no
        self.__test_mark = ''
        self.__exam_mark = ''
        while type(self.__test_mark) != int:
            try:
                self.__test_mark = int(input("Enter Test mark: "))
            except ValueError:
                print("Invalid Input Type!")
        while type(self.__exam_mark) != int:
            try:
                self.__exam_mark = int(input("Enter Exam mark: "))
            except ValueError:
                print("Invalid Input Type!")

    def computeFinalMark(self):
        return (self.__exam_mark+self.__test_mark)/2
    def __str__(self):
        return f"{self.get_name()}, Admin No: {self.__admin_no} final mark is {Student.computeFinalMark(self):.2f}"

