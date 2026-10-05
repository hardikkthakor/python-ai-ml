


#Q1 — Squares Dictionary
numbers = [1, 2, 3, 4]


squares_num = {
    num: num ** 2 
    for num in numbers
}

print(squares_num)


#Q2 — Even Numbers Only
numbers = [1, 2, 3, 4, 5, 6]

even_num = {
    num: num * 10
    for num in numbers
    if num % 2 == 0
}
print(even_num)


#Q3 — Number Status
numbers = [1, 2, 3, 4, 5]

even_odd = {
    num: "Even" if num % 2 == 0 else "Odd"
    for num in numbers
}
print(even_odd)

#Q4 — Student Bonus
students = {
    "hardik": 85,
    "rahul": 72,
    "priya": 95
}

student = {
    name.upper(): mark + 5 
    for name, mark in students.items()
}
print(student)


#Q5 — Passed Students
students = {
    "Hardik": 85,
    "Rahul": 35,
    "Priya": 72,
    "Amit": 25
}

new_student_dict = {
    name: "Pass" for name, marks in students.items()
    if marks >=40
}
print(new_student_dict)




#Q6 — Clean Skills

skills = ["python", "Python", "", "  ", "ai", "machine learning"]

skill_dict = {
    skill.strip().upper(): len(skill.strip())
    for skill in skills 
    if skill.strip() != ""
}
print(skill_dict)


#Q7 — Product Discount
products = {
    "laptop": 50000,
    "mouse": 1000,
    "keyboard": 2500,
    "monitor": 15000
}

discount_product = {
    product.upper(): price * 0.9 
    for product, price in products.items()
    if price >=2000
}

print(discount_product)


#Q8 — Student Result
students = {
    "Hardik": 85,
    "Rahul": 35,
    "Priya": 72,
    "Amit": 25,
    "Neha": 95
}

result = {
    name: "Pass" if marks >= 40 else "Fail" 
    for name, marks in students.items()
} 

print(result)


#Q9 — Employee Salary Bonus
employees = {
    "hardik": 30000,
    "rahul": 18000,
    "priya": 45000,
    "amit": 22000
}

emp_bonus = {
    name.upper() : salary + 5000 
    for name, salary in employees.items()
    if salary >= 25000
}
print(emp_bonus)


#Q10 — Number Analyzer
numbers = [-5, 0, 10, -2, 7]

num_analyzer = {
    num: "Positive" if num > 0 else "Negative" if num < 0 else "Zero"
    for num in numbers
}

print(num_analyzer)




#==================================Dictionary Comprehension — Exercises=========================



#Exercise 1 — Number and Double
numbers = [2, 4, 6, 8, 10]

double = {
    num: num * 2
    for num in numbers
}

print(double)


#Exercise 2 — Positive Number Squares
numbers = [-5, 2, -3, 4, 0, 6]

cleaned_num = {
    num: num ** 2 
    for num in numbers
    if num > 0
}
print(cleaned_num)


#Exercise 3 — Even/Odd Dictionary
numbers = [5, 10, 7, 12, 3]

check_num = {
    num: "Even" if num % 2 == 0 else "Odd"
    for num in numbers
}

print(check_num)


#numbers = [5, 10, 7, 12, 3]

students = {
    "Hardik": 95,
    "Rahul": 82,
    "Priya": 67,
    "Amit": 35
}

grades = {
    name: "A" if marks >= 80 else "B" if marks >= 60 else "Fail"
    for name, marks in students.items()
}

print(grades)


#Exercise 5 — Uppercase Products

products = {
    "laptop": 50000,
    "mouse": 1000,
    "keyboard": 2500,
    "monitor": 15000
}

updated_product = {
    product.upper(): price
    for product, price in products.items()
    if price >= 2000
}

print(updated_product)


#Exercise 6 — Salary Bonus

employees = {
    "hardik": 30000,
    "rahul": 18000,
    "priya": 45000,
    "amit": 22000
}

salary_bonus = {
    name.upper(): salary + salary * 0.10 
    for name, salary in employees.items()
    if salary >= 20000
}

print(salary_bonus)


#Exercise 7 — Clean Skills Dictionary

skills = [
    "python",
    "Python",
    "",
    "  ",
    "ai",
    "machine learning",
    "AI"
]

cleaned_skills = {
    skill.strip().upper(): len(skill.strip())
    for skill in skills
    if skill.strip() != ""
}
print(cleaned_skills)


#Exercise 8 — Marks Analyzer

marks = {
    "Hardik": 85,
    "Rahul": 35,
    "Priya": 72,
    "Amit": 25,
    "Neha": 95
}

analyze_marks = {
    name.upper(): "Excellent" if mark >=80 else "Good" if mark >=60 else "Pass"
    for name, mark in marks.items()
    if mark >=40
}

print(analyze_marks)





#====================================================================
            #Mini Project — Student Performance Analyzer
#====================================================================

students = {
    "Hardik": 85,
    "Rahul": 35,
    "Priya": 72,
    "Amit": 25,
    "Neha": 95,
    "Riya": 60,
    "Karan": 40
}

passed_students = {
    name: marks 
    for name, marks in students.items()
    if marks >= 40
}

failed_students = {
    name: marks 
    for name, marks in students.items()
    if marks < 40
}

students_results = {
    name: "Pass" if marks >= 40 else "Fail"
    for name, marks in students.items()
}

students_grades = {
    name: "A+" if marks >= 90 
    else "A" if marks >= 80 
    else "B" if marks >= 70 
    else "C" if marks >= 60
    else "D" if marks >= 40
    else "F"
    for name, marks in students.items()
}

uppercase_bonus = {
    name.upper(): marks + 5 
    for name, marks in students.items()
    if marks >= 40
}


print("========== STUDENT PERFORMANCE ANALYZER ==========\n")

print(f"All Students:\n {students}")
print(f"Passed Students:\n {passed_students}")
print(f"Failed Students:\n {failed_students}")
print(f"Results:\n {students_results}")
print(f"Grades:\n {students_grades}")
print(f"Passed Students With Bonus:\n {uppercase_bonus}")