



                                            #Project: Student Management System

from student_management.student_info import get_student_details
from student_management.student_result import calculate_percentage, get_result

name = input("Enter Student Name: ")
age = int(input("Enter Age: "))
course = input("Enter Course: ")
marks_4_sub = input("Enter Four Subjects Marks: ").split()
marks_4_sub = [int(marks) for marks in marks_4_sub]

print("=========== STUDENT MANAGEMENT SYSTEM ===========")
print(get_student_details(name, age, course))

percentage = calculate_percentage(marks_4_sub)
print("Percentage: ", percentage)
print("Result: ", get_result(percentage))
