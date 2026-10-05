



from employee_package.employee_info import employee_details, employee_role
from employee_package.employee_tools import is_eligible, calculate_bonus

name = input("Enter Name: ")
age = int(input("Enter Age: "))
role = input("Enter Role: ")
salary = float(input("Enter Salary: "))

print("=======================EMPLOYEE DETAILS=====================")
print(employee_details(name, age))
print(employee_role(role))
print("Eligible:",is_eligible(age))
print("Bonus:",calculate_bonus(salary))