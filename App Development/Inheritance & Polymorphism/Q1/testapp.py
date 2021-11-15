import Lecturer as l
import Student as s


name = input("Enter Lecturer name: ")
nric = input("Enter Lecturer NRIC: ")
staff_id = input("Enter Staff ID: ")
hour = float(input("Enter Total Teaching Hours: "))
lecturer = l.Lecturer(name, nric, staff_id)
lecturer.set_total_TeachingHour(hour)

input_name = input("Enter Student name: ")
input_nric = input("Enter Student NRIC: ")
input_admin_no = input("Enter Student Admin Number: ")
input_test_marks = float(input("Enter Test Marks: "))
input_exam_marks = float(input("Enter Exam Marks: "))
student = s.Student(input_name,input_nric,input_admin_no)
student.set_test_mark(input_test_marks)
student.set_exam_mark(input_exam_marks)

print(lecturer)
print(student)
