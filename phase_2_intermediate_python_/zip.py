


#============================================
                #ZIP()
#============================================

"""
# Q1 — Write code
# Pair each student with their mark using zip().
students = ["Hardik", "Aman", "Riya"]

marks = [85, 72, 91]

result = list(zip(students,marks))
print(result)

# Q3 — Write code
# Combine names, marks, and grades using zip().
names = ["Aman", "Riya", "Karan"]

marks = [78, 92, 65]

grades = ["B+", "A+", "B"]

results = list(zip(names,marks,grades))
print(results)


# Q4 — Write code
# Create a dictionary by pairing keys and values with zip().
keys = ["name", "age", "city"]

values = ["Hardik", 20, "Delhi"]

result = dict(zip(keys,values))
print(result)


# Q1
# Pair each product with its price.
products = ["Laptop", "Mouse", "Keyboard"]

prices = [55000, 700, 1500]

pair_items = list(zip(products,prices))
print(pair_items)

# Q2
# Pair names, ages, and cities.
names = ["Hardik", "Aman", "Riya"]

ages = [20, 21, 19]

cities = ["Delhi", "Mumbai", "Pune"]

combine = list(zip(names,ages,cities))
print(combine)

# Q3
# Create a dictionary using zip().
subjects = ["Python", "Java", "SQL"]

marks = [92, 85, 88]

dictionary = dict(zip(subjects,marks))
print(dictionary)

# Q5
# Use zip() with a for loop to print each student and mark.
students = ["Hardik", "Aman", "Riya"]

marks = [85, 72, 91]

for student, mark in zip(students,marks):
    print(student,mark)
"""

#8. Real-World Mini Project — Student Performance Report============

students = ["Hardik", "Aman", "Riya", "Karan"]

marks = [85, 72, 91, 65]

attendance = [90, 75, 95, 80]

students_data = list(zip(students,marks,attendance))
print(students_data)
for student in zip(students,marks,attendance):
    print(student)

dictionary = dict(zip(students,marks))
print(dictionary)


# Q10
# Pair each country with its capital using zip().
countries = ["India", "Japan", "France"]

capitals = ["New Delhi", "Tokyo", "Paris"]

pairing = list(zip(countries,capitals))
print(pairing)

# Q11
# Create a dictionary using zip().
languages = ["Python", "Java", "JavaScript"]

levels = ["Beginner", "Intermediate", "Beginner"]

result = dict(zip(languages,levels))
print(result)


# Q12
# Use zip() with a for loop to print each product and price.
products = ["Laptop", "Mouse", "Keyboard"]

prices = [55000, 700, 1500]

for product, price in zip(products,prices):
    print(product,":",price)


# Q13
# Combine names, marks, and attendance using zip().
# Print every student's details in a for loop.
names = ["Hardik", "Aman", "Riya"]

marks = [85, 72, 91]

attendance = [90, 75, 95]

data = list(zip(names,marks,attendance))
print(data)

for student in zip(names,marks,attendance):
    print(student)