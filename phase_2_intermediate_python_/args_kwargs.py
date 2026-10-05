

                            #===============================================================================
                                                            # args() & kwargs()
                            #===============================================================================

#Mixed Practice — *args + **kwargs
"""
#Q1 — Sum of Numbers
def calculate_sum(*numbers):

    total = sum(numbers)
    print("Total: ",total)
calculate_sum(10,20,30,40,50)


#Q2 — Find Even Numbers
def find_even(*numbers):

    for num in numbers:
        if num % 2 == 0:
            print(num)
find_even(10,13,18,20,43,50)


#Q3 — Student Details
def student_details(name, **details):

    print("Name: ", name)
    print("Details: ")
    for key, value in details.items():
        print(f"{key} : {value}")

student_details(
    "Hardik",
    age= 24,
    city="Ahmedabad",
    course="Python AI/ML"
)


#Q4 — Employee Skills
def employee(name, employee_id, *skills):

    print("Name: ",name)
    print("Employee ID: ",employee_id)
    print("Skills: ")

    for index, skill in enumerate(skills, start=1):
        print(f"{index}. {skill}")

employee(
    "Hardik",
    904,
    "Python",
    "SQL",
    "Machine Learning"
)


#Q5 —  Employee Profile Analyzer
def employee_profile(name, employee_id, *skills, **details):

    print("========== EMPLOYEE PROFILE ==========\n")
    print("Name: ",name)
    print(f"Emp ID: {employee_id}\n")
    print("Skills: ") 

    for index,skill in enumerate(skills, start=1):
        print(f"{index}. {skill}")
    
    print("\nAdditional Details:")
    for key,value in details.items():
        print(f"{key} : {value}")

employee_profile(
    "Hardik",
    121,
    "Python",
    "SQL",
    "AI/ML",
    city="Ahmedavad",
    experience=1,
    education="BCA"
)
"""


                                                    #Exercises — *args & **kwargs
"""
#Exercise 1 — Number Analyzer
def analyze_numbers(*numbers):

    print(f"Numbers: {numbers}")

    largest = numbers[0]
    smallest = numbers[0]
    even_count = 0
    odd_count = 0
    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        
        if num > largest:
            largest = num
        elif num < smallest:
            smallest = num
        
    total = sum(numbers)
    average = total / len(numbers)

    print("Total: ",total)
    print("Average: ",average)
    print("Largest: ",largest)
    print("Smallest: ",smallest)
    print("Even Count: ",even_count)
    print("Odd Count: ",odd_count)

analyze_numbers(10, 25, 40, 15, 30)


#Exercise 2 — Student Result Analyzer
def student_result(name, *marks):
    print("========== STUDENT RESULT ==========\n")
    print(f"Name: {name}\n")
    print("Marks: ")
    for index,mark in enumerate(marks, start=1):
        print(f"{index}. {mark}")

    total = sum(marks)
    average = total / len(marks)

    if average >= 40:
        result = "Pass"
    else:
        result = "Fail"

    print(f"\nTotal: {total}")
    print(f"Average: {average}")
    print(f"Result: {result}")

student_result(
    "Hardik",
    85,
    72,
    65,
    90,
    78
)


#Exercise 3 — Employee Information
def employee_info(name, employee_id, **details):

    print("========== EMPLOYEE INFORMATION ==========\n")
    print(f"Name: {name}")
    print(f"Employee ID: {employee_id}")
    print(f"\nAdditional Details: ")
    for key,value in details.items():
        print(f"{key} : {value}")

employee_info(
    "Hardik",
    101,
    department="AI/ML",
    city="Ahmedabad",
    experience=1,
    education="BCA"
)


#Exercise 4 — Product Price Analyzer
def product_analyzer(*prices):
    
    print("========== PRODUCT ANALYZER ==========\n")
    
    for index,price in enumerate(prices, start=1):
        print(f"Product {index}: ₹{price}")

    highest = prices[0]
    lowest = prices[0]
    cost_count_high = 0
    cost_count_low = 0
    for price in prices:

        if price > highest:
            highest = price
        elif price < lowest:
            lowest = price
        
        if price >= 1000:
            cost_count_high += 1
        else:
            cost_count_low += 1

    total = sum(prices)

    print(f"\nTotal: ₹{total}")
    print(f"Highest: ₹{highest}")
    print(f"Lowest: ₹{lowest}")
    print(f"Premium Products: {cost_count_high}")
    print(f"Regular Products: {cost_count_low}")

product_analyzer(500, 1500, 750, 2000, 1200)


#Exercise 5 — Employee Profile Analyzer

def employee_profile(name, employee_id, *skills, **details):

    print("========== EMPLOYEE PROFILE ==========\n")

    print(f"Name: {name}")
    print(f"Employee ID: {employee_id}\n")

    print("Skills: ")
    for index,skill in enumerate(skills, start= 1):
        print(f"{index}. {skill}")

    print(f"\nAdditional Details: ")
    for key,value in details.items():
        print(f"{key} : {value}")
    
        if len(skills) >= 3:
            skill_level = "Multi-Skilled"
        else:
            skill_level = "Developing"
    
    print(f"\nSkill Level: {skill_level}")

employee_profile(
    "Hardik",
    101,
    "Python",
    "SQL",
    "Machine Learning",
    "AI",
    city="Ahmedabad",
    education="BCA",
    experience=1
)
"""


#=====================================================================================
"""
#Mini Project — Employee Profile & Skill Analyzer

def employee_analyzer(name,employee_id,*skills,**details):
    print("========== EMPLOYEE ANALYZER ==========\n")
    print(f"Employee Name: {name}")
    print(f"Employee ID: {employee_id}\n")
    print(f"Skills: ")
    skill_count = 0
    for index,skill in enumerate(skills, start= 1):
        print(f"{index}. {skill}")
        skill_count += 1
    print(f"\nTotal Skills: {skill_count}")

    if len(skills) >= 3:
        skill_level = "Multi-Skilled"
    else:
        skill_level = "Developing"

    print(f"Skill Level: {skill_level}")

    print(f"\nAdditional Details: ")
    for key,value in details.items():
        print(f"{key} : {value}")

    experience = details["experience"]
    if experience >= 2:
        experience_status = "Experienced"
    else:
        experience_status = "Junior"
    print(f"\nExperience Status: {experience_status}")

employee_analyzer(
    "Hardik",
    111,
    "Python",
    "SQL",
    "Machine Learning",
    "AI/ML",
    city="Ahmedabad",
    education="BCA",
    experience=2
)
"""

#1

def analyze(*numbers):

    even_count = 0
    odd_count = 0
    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        
    total = sum(numbers)
    average = total / len(numbers)
    
    print(f"Total: {total}")
    print(f"Average: {average}")
    print(f"Even Count: {even_count}")
    print(f"Odd Count: {odd_count}")
analyze(10,15,20,25,30)


#2

def profile(name,*skills,**details):
    print("========================PROFILE======================\n")
    print(f"Name: {name}\n")
    print(f"Skills: ")
    skill_count = 0
    for index,skill in enumerate(skills, start= 1):
        print(f"{index}. {skill}")
        skill_count += 1
    print(f"Total Skills: {skill_count}")

    print(f"\nAdditional Details: ")
    for key,value in details.items():
        print(f"{key} : {value}")
    
    if len(skills) >= 3:
        skill_level = "Multi-Skilled"
    else:
        skill_level = "Developing"
    
    print(f"\nSkill Level: {skill_level}")

profile(
    "Hardik",
    "Python",
    "SQL",
    "AI",
    "Machine Learning",
    city="Ahmedabad",
    experience=3,
    education="BCA"
)