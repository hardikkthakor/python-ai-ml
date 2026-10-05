

#=======================================================================
                            #enumerate()
#=======================================================================
"""
# Q1 — Write code
# Print each language with numbering starting from 1.
languages = ["Python", "Java", "SQL"]

for index, language in enumerate(languages, start=1):
    print(index,":",language)

# Q3 — Write code
# Create a numbered task list beginning at 1.
tasks = ["Learn Python", "Practice Coding", "Build Projects"]

result = list(enumerate(tasks, start=1))
print(result)


# Q1----------------------------------------------------------------------------------
# Print each movie with numbering starting from 1.
movies = ["Inception", "Interstellar", "Avatar", "Titanic"]

for index,movie in enumerate(movies, start=1):
    print(index,":",movie)


# Q2
# Create a list of index-item tuples starting from index 10.
cities = ["Delhi", "Mumbai", "Pune"]
result = list(enumerate(cities,start=10))
print(result)

# Q3
# Print only the items at even indexes: 0, 2, 4, ...
numbers = [10, 20, 30, 40, 50, 60]

for index, number in enumerate(numbers):
    if index % 2 == 0:
        print(index, ":", number)

# Q4
# Find and print the index of "Python".
languages = ["Java", "C++", "Python", "JavaScript"]
for index,language in enumerate(languages):
    if language == "Python":
        print(index)

# Q5
# Print a numbered product-price report starting from 1.
products = ["Laptop", "Mouse", "Keyboard"]

prices = [55000, 700, 1500]

for number,(product,price) in enumerate(zip(products,prices),start=1):
    print(number, product,price)
"""

#8. Real-World Mini Project — Store Inventory Report
"""
products = ["Laptop", "Mouse", "Keyboard", "Monitor"]
prices = [55000, 700, 1500, 12000]
stock = [5, 20, 12, 8]


for serial, (product, price, item_stock) in enumerate(
    zip(products, prices, stock), start=1
):
    print(f"{serial}. {product} - Price: {price}, Stock: {item_stock}")

    if item_stock < 10:
        print("Low Stock!!!")
"""

"""
#practice
#1
fruits = ["Apple", "Banana", "Mango", "Orange"]

for index, fruit in enumerate(fruits):
    print(index,":",fruit)

#2 start from 1
subjects = ["Python", "Math", "English", "AI"]

for index, sub in enumerate(subjects, start=1):
    print(index,":",sub)

#3
students = ["Hardik", "Rahul", "Priya", "Amit"]

for index, student in enumerate(students, start=1):
    print("Student",index,":",student)

#4 find index of javascript  (Find a specific item)
languages = ["Python", "Java", "C++", "JavaScript", "C#"]

for index, language in enumerate(languages):
    if language == "JavaScript":
        print(language,"is at index :",index)
    
#Q5 — Practical: Number Analyzer
numbers = [10, 25, 40, 55, 80]

for index, num in enumerate(numbers):
    if num % 2 == 0:
        status= "Even"
    else:
        status = "Odd"
    print(f"Position {index}: {num} - {status}")
"""

#PRACTICE
"""#Q1. Student Result

students = ["Hardik", "Rahul", "Priya", "Amit"]
marks = [85, 42, 76, 31]

for index,(student,mark) in enumerate(zip(students,marks),start=1):
    if mark >= 40:
        status = "Pass"
    else:
        status = "Fail"

    print(f"{index}. {student} - {mark} - {status}")


#Q2. Even/Odd with Position
numbers = [12, 7, 24, 15, 30]

for index,num in enumerate(numbers, start=1):
    if num % 2 == 0:
        status = "Even"
    else:
        status = "Odd"
    
    print(f"{index}. {num} - {status}")

#Q3. Find a Name
names = ["Rahul", "Priya", "Hardik", "Amit"]

for index,name in enumerate(names, start=1):
    if name == "Hardik":
        print(f"Hardik Found At Position: {index}")
    

#Q4. Number Analyzer
numbers = [10, -5, 0, 25, -12]

for index, num in enumerate(numbers, start=1):
    if num > 0:
        status = "Positive"
    elif num < 0:
        status = "Negative"
    else:
        status = "Zero"

    print(f"{index}. {num} - {status}")


#Q5. Slightly Challenging
prices = [500, 1200, 750, 2000]

for index, price in enumerate(prices, start= 1):
    if price >= 1000:
        status = "Premium"
    else:
        status = "Regular"
    
    print(f"Product {index}. {price} - {status}")
"""

#===================================================================================================
                        #Student Attendance & Performance Tracker
#===================================================================================================

students = ["Hardik", "Rahul", "Priya", "Amit", "Neha"]
marks = [85, 42, 76, 31, 92]
attendance = [90, 65, 82, 55, 95]
print("========== STUDENT REPORT ==========")
for number, (student, mark,attend) in enumerate(zip(students,marks,attendance), start= 1):
    if mark >= 40:
        result = "Pass"
    else:
        result = "Fail"
    
    if attend >= 75:
        status = "Good"
    else:
        status = "Low"

    if mark >= 40 and attend >= 75:
        eligibility = "Eligible"
    else:
        eligibility = "Not Eligible"
    
    print(f"{number}. {student}\n   Marks: {mark}\n   Attendance: {attend}%\n   Result: {result}\n   Attendance Status: {status}\n   Exam Eligibility: {eligibility}\n")

