

#=======================================================================
                            #List Comprehension
#=======================================================================
"""
#Q1 — Square Numbers

numbers = [1, 2, 3, 4, 5]

squares = [number ** 2 for number in numbers]
print(squares)


#Q2 — Filter Even Numbers

numbers = [10, 15, 20, 25, 30, 35]

even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)


#Q3 — Pass or Fail

marks = [85, 35, 60, 20, 75]

results = ["Pass" if mark >=40 else "Fail" for mark in marks]
print(results)


#Q4 — Filter and Transform

numbers = [2, 5, 8, 11, 14, 17]

answer = [number ** 2 for number in numbers if number > 10]
print(answer)


#Q5 — Names

names = ["hardik", "ai", "python", "ml", "data"]

uppercase_names = [name.upper() for name in names if len(name) >= 4]
print(uppercase_names)


#Q6 — Positive Numbers

numbers = [-10, 5, -3, 8, 0, 12, -7]

positive_numbers = [number for number in numbers if number > 0]
print(positive_numbers)


#Q7 — Temperature Conversion

celsius = [0, 10, 20, 30, 40]

fahrenheit = [(temp * 9 / 5) + 32 for temp in celsius]
print(fahrenheit)


#Q8 — Student Result

marks = [95, 72, 38, 55, 20, 88]

results = ["Pass" if mark >= 40 else "Fail" for mark in marks]
print(results)


#Q9 — Even Squares

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even_squares = [number ** 2 for number in numbers if number % 2 == 0]
print(even_squares)


#Q10 — Clean Names

names = ["hardik", "", "rahul", "ai", "", "python"]

new_list = [name.upper() for name in names if name != ""]
print(new_list)


#Q11 — Number Classification

numbers = [-5, 0, 10, -2, 7]

classification = [
    "Positive" if num > 0 else "Negative" if num < 0  else "Zero" 
    for num in numbers
    ]

print(classification)
"""


#=========================================================
            #List Comprehensions — Exercises
#=========================================================
"""
#Exercise 1 — Double the Numbers

numbers = [3, 6, 9, 12, 15]

double = [number * 2 for number in numbers]
print(double)


#Exercise 2 — Numbers Divisible by 3

numbers = [1, 3, 5, 6, 8, 9, 12, 14, 15]

new_list = [number for number in numbers if number % 3 == 0]
print(new_list)


#Exercise 3 — Square Positive Numbers

numbers = [-4, 2, -1, 5, 0, 3, -7]

ps_square = [number ** 2 for number in numbers if number > 0]
print(ps_square)


#Exercise 4 — Convert to Uppercase

languages = ["python", "java", "ai", "machine learning"]

uppercase_lang = [lang.upper() for lang in languages]
print(uppercase_lang)


#Exercise 5 — Long Words

words = ["AI", "Python", "ML", "Developer", "Data", "Code"]

long_words = [word for word in words if len(word) > 4 ]

print(long_words)


#Exercise 6 — Even or Odd

numbers = [10, 7, 4, 9, 12]

num = ["Even" if num % 2 == 0 else "Odd" for num in numbers]
print(num)


#Exercise 7 — Marks Classification

marks = [95, 82, 67, 45, 39, 20]

result = [
    "Excellent" if mark >= 80 else "Good" if mark >=60 else "Pass" if mark >=40 else "Fail" 
    for mark in marks
    ]

print(result)


#Exercise 8 — Clean and Format Names

names = ["hardik", "", "rahul", "  ", "priya", "ai"]

updated_name = [name.upper() for name in names if name.strip() !=""]
print(updated_name)


#Exercise 9 — Price Discount

prices = [500, 1200, 800, 1500, 300]

discount_price = [price * 0.9 if price >=1000 else price for price in prices]
print(discount_price)


#Exercise 10 — Number Analyzer

numbers = [-10, 0, 5, 12, -3, 8, 0]

positive_list = [num for num in numbers if num > 0]
negative_list = [num for num in numbers if num < 0]
status = [
    "Positive" if num > 0 else "Negative" if num < 0 else "Zero" 
    for num in numbers
    ]

print(positive_list)
print(negative_list)
print(status)
"""

                                    #Mini Project — Student Marks Analyzer
"""
marks = [85, 32, 67, 95, 40, 28, 76, 55, 100, 15]


passed_marks = [mark for mark in marks if mark >= 40]

failed_marks = [mark for mark in marks if mark < 40]

results = ["Pass" if mark >=40 else "Fail" for mark in marks]

grades = [
    "A+" if mark >=90
    else "A" if mark >=80
    else "B" if mark >=70
    else "C" if mark >=60
    else "D" if mark >=40
    else "F" 
    
    for mark in marks
]

print("===== STUDENT MARKS ANALYZER =====")

print("All Marks: ", marks)

print("Passed Marks: ", passed_marks)
print("Failed Marks: ", failed_marks)

print("Results: ", results)
print("Grades: ",grades)
"""