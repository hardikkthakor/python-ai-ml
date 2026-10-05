



#Exercise 1 — Math Helper

# import math

# num = float(input("Enter Number :"))

# if num < 0:
#     print("Invalid Input!!")
# else:
#     print("Square Root :", math.sqrt(num))
#     print("Power of 2 :", math.pow(num, 2))
#     print("Floor :", math.floor(num))


#Exercise 2 — Lucky Number

import random

lucky_number = random.randint(1,50)
guess_number = 0

while guess_number != random:
    guess_number = int(input("Enter Guess Number :"))

    if guess_number == random:
        print("Correct Guess!!")
    else:
        print("Wrong!!! Lucky number was:", lucky_number)


#Exercise 3 — Date Information

import datetime

now = datetime.datetime.now()

print(now.strftime("%d-%m-%Y"))
print(now.strftime("%B %d, %Y"))
print(now.strftime("%a"))

#Exercise 4 — Custom Utility Module-------(Work in Main.py)
# from my_module import cube,is_even

# number = int(input("Enter Number :"))

# print(cube(number))
# print(is_even(number))

#Exercise 5 — Module Challenge
import random
import datetime

messages = [
    "Keep Learning!",
    "Never Give Up!",
    "Python is Powerful!",
    "Practice Makes Perfect!"
]

selected_message = random.choice(messages)

print("Today's Motivation :",selected_message)

now = datetime.datetime.now()
print(now.strftime("%d-%m-%Y"))



