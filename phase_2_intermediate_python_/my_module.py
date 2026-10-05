#=======================================================================================
                                            #MODULES 
#=======================================================================================


                                            #1. Math Module

import math

print(math.sqrt(144))
print(math.ceil(9.2))


                                            #strftime() for DATE & TIME

import datetime

now = datetime.datetime.now()

print(now.strftime("%d %B, %Y"))
print(now.strftime("%H:%M:%S"))


                            #own module practically

def greet(name):
    return f"Hello, {name}!"

def square(number):
    return number ** 2


#Task 1 — math
import math

print(math.sqrt(225))
print(math.ceil(7.3))
print(math.floor(7.9))

#Task 2 — random
import random

names = ["Hardik", "Rahul", "Priya", "Amit"]

one = random.choice(names)
print(one)

random.shuffle(names)
print(names)

#Task 3 — datetime
import datetime

now = datetime.datetime.now()
print(now.strftime("%d %B, %Y"))
print(now.strftime("%H:%M:%S"))


#Task 4 — Your User-Defined Module 
#(ANS IN THE MAIN.PY)


                                            # 1 — Random Number Checker

import random

number = random.randint(1, 100)

def check_number(number):
    if number % 2 == 0:
        print("Number is Even")
    else:
        print("Number is Odd")
    
    if number > 0:
        print("Number is Positive")
    elif number < 0:
        print("Number is Negative")
    else:
        print("Number is Zero")

check_number(number)

                                                    #2 — Math Calculator

import math

num = float(input("Enter Your Number: "))
if num < 0:
    print("Invalid Input")
else:
    print("Square Root: ", math.sqrt(num))
    print("Ceiling: ", math.ceil(num))
    print("Floor: ", math.floor(num))

                                                    #3 — Random Student Picker

import random

students = ["Hardik", "Rahul", "Priya", "Amit", "Neha"]

def select_student(students):

    selected = random.choice(students)
    print(selected)

select_student(students)

#=====================================================================
#Exercise 4 — Custom Utility Module   exercise.py and my_module =.py
#=====================================================================

def cube(number):
    return number ** 3

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
