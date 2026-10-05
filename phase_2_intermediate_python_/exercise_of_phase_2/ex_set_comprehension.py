"""

#Q9 — Unique Positive Squares

numbers = [-3, 2, 2, 4, -1, 5, 4]

positive_squares = {
    num ** 2 for num in numbers if num > 0
}
print(positive_squares)

#Q10 — Clean Unique Languages
languages = [
    "python",
    "Python",
    "",
    "  ",
    "java",
    "JAVA",
    "ai"
]

updated_set = {
    language.strip().upper() for language in languages
    if language.strip() != "" 
}
print(updated_set)

#Q11 — Grade Categories

marks = [95, 75, 65, 45, 30, 95]

grades = {
    "Excellent" if mark >=80
    else "Good" if mark >=60
    else "Pass" if mark >=40
    else "Fail"
    for mark in marks   
}
print(grades)







#======================================================
        #Combined Revision Test — Part 2: Coding
#======================================================

#Q1 — List Comprehension
numbers = [-2, 1, 2, 3, 4, -5]

pos_square = [num ** 2 for num in numbers if num > 0]
print(pos_square)


#Q2 — Set Comprehension
numbers = [1, 2, 2, 3, 4, 4, 5, 6]

even_square = {
    num ** 2 for num in numbers 
    if num % 2 == 0
}
print(even_square)

#Q3 — List Comprehension with if-else
numbers = [-5, 0, 10, -2, 7]

pos_neg = [
    "Positive" if num > 0 else "Negative" if num < 0 else "Zero"
    for num in numbers
]
print(pos_neg)


#Q4 — Set Comprehension
names = ["hardik", "Hardik", "", "  ", "python", "PYTHON", "ai"]

updated_names = {
    name.stip().upper()
    for name in names
    if name.strip()
}
print(updated_names)


#Q5 — Dictionary Comprehension
students = {
    "hardik": 85,
    "rahul": 35,
    "priya": 72,
    "amit": 25,
    "neha": 95
}

uppercase_students = {
    name.upper(): 
    "Excellent" if marks >= 80 else "Good" if marks >= 60 else "Pass"
    for name,marks in students.items() 
    if marks >= 40
 }
print(uppercase_students)
"""

