



#=========================================================================
                #LAMBDA
#=========================================================================

"""
#Q1 — Square
square = lambda num: num ** 2
print(square(5))


#Q2 — Addition
add = lambda a,b: a + b
print(add(10,20))


#Q3 — Even or Odd
check_even_odd = lambda num: "Even" if num % 2 == 0 else "Odd"
print(check_even_odd(7))


#Q4 — Maximum Number
maximum = lambda a,b: a if a > b else b
print(maximum(50,30))


#Q5 — Greeting
greet = lambda : "Hello, Hardik!"
print(greet())


#Q1 — Multiply
multiply = lambda a,b: a * b
print(multiply(6,7))


#Q2 — Positive, Negative, or Zero
check_number = lambda num: "Positive" if num > 0 else "Negative" if num < 0 else "Zero"
print(check_number(-5))
print(check_number(0))
print(check_number(10))


#Q3 — Eligible or Not Eligible
check_age = lambda age: "Eligible" if age >= 18 else "Not Eligible"
print(check_age(20))
print(check_age(15))


#Q4 — Grade Checker
grade = lambda marks: "A" if marks >= 80 else "B" if marks >= 60 else "C" if marks >= 40 else "Fail"
print(grade(99))
print(grade(21))
print(grade(40))
print(grade(65))


#Q5 — Simple Interest
simple_interest = lambda principal,rate,time: (principal * rate * time) / 100
print(simple_interest(10000,5,2))
"""

"""
#Exercise 1 — Triple a Number
triple = lambda num: num * 3 
print(triple(7))


#Exercise 2 — Check Divisibility
is_divisible = lambda num, divisor: "Divisible" if num % divisor == 0 else "Not Divisible"
print(is_divisible(20,3))
print(is_divisible(17,3))


#Exercise 3 — Find Minimum
minimum = lambda a,b: a if a < b else b
print(minimum(25,10))
print(minimum(5,18))


#Exercise 4 — Temperature Status
temperature_status = lambda temperature: "Hot" if temperature >= 35 else "Normal" if temperature >= 20 else "Cold"
print(temperature_status(40))
print(temperature_status(25))
print(temperature_status(15))


#Exercise 5 — Student Result
student_result = lambda marks: "Excellent" if marks >= 80 else "Good" if marks >= 60 else "Pass" if marks >= 40 else "Fail"
print(student_result(99))
print(student_result(21))
print(student_result(40))
print(student_result(65))
print(student_result(80))


#Exercise 6 — Discount Calculator
discount_price = lambda price: price * 0.9 if price >= 1000 else price
print(discount_price(1500))
print(discount_price(500))


#Exercise 7 — Salary Bonus
salary_bonus = lambda salary: salary * 1.10 if salary >=30000 else salary
print(salary_bonus(40000))
print(salary_bonus(20000))


#Exercise 8 — Name Formatter
format_name = lambda name: name.strip().upper()
print(format_name("  hardik  "))
print(format_name(" python "))


#Exercise 9 — Number Analyzer
number_status = lambda num: "Zero" if num == 0 else "Negative" if num < 0 else "Positive Even" if num % 2 == 0 else "Positive Odd"
print(number_status(10))
print(number_status(7))
print(number_status(-5))
print(number_status(0))


#Exercise 10 — Student Eligibility
student_eligibility = lambda age, marks: "Eligible" if age >=18 and marks >= 40 else "Not Eligible"
print(student_eligibility(23,98))
print(student_eligibility(17,21))
"""



#Mini Project: Employee Salary Analyzer
"""
salaries = [18000, 25000, 30000, 45000, 55000]

#calculate bonus
calculate_bonus = lambda salary: salary + salary * 0.10 if salary >= 30000 else salary

#salary status
salary_status = lambda salary: "High" if salary >= 50000 else "Medium" if salary >= 30000 else "Basic"

#is_eligible
is_eligible = lambda salary: "Eligible" if salary >= 25000 else "Not Eligible"

print("========== EMPLOYEE SALARY ANALYZER ==========\n")

for salary in salaries:
    print(f"Original Salary: {salary}")
    print(f"Salary With Bonus: {calculate_bonus(salary)}")
    print(f"Salary Status: {salary_status(salary)}")
    print(f"Eligibility: {is_eligible(salary)}")
    print()
"""
