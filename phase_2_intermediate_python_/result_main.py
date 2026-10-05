
                                                    
                                                    #Exercise 2 — Student Result Package


from result_package.student import student_info
from result_package.result import check_result, get_grade

name = input("Enter Your Name: ")
marks = int(input("Enter Your Marks: "))

print(student_info(name,marks))
print(check_result(marks))
print(get_grade(marks))