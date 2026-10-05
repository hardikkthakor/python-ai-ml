



#==============================================================================
                #Advanced Exception Handling — Mixed Practice
#==============================================================================


                                #Exercise 1 — Safe Division
"""
try: 
    num1 = int(input("Enter Number 1: "))
    num2 = int(input("Enter Number 2: "))
    result = num1 / num2
except ValueError:
    print("Please enter valid numbers.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("Result: ", result)
finally:
    print("Program finished.")

                                    #Exercise 2 — Student Marks Validator
try:
    marks = float(input("Enter Marks: "))

    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100.")
except ValueError:
    print("Invalid Input!")
else:
    print("Valid Marks: ", marks)

                                    #Exercise 3 — Safe List Access

numbers = [10, 20, 30, 40, 50]
try:

    user_input = input("Enter Index: ")
    index = int(user_input)
    selected_number = numbers[index]

except ValueError:
    print("invalid index input!")
except IndexError:
    print("index does not exists!")
else:
    print("Selected Number: ",selected_number )
finally:
    print("Program finished.")


                                        #Exercise 4 — Dictionary Lookup

student = {
    "name": "Hardik",
    "course": "Python AI/ML",
    "city": "Ahmedabad"
}

user_input = input("Enter Key: ")

try:
    print(student[user_input])
except KeyError:
    print(f"KeyError: The key '{user_input}' does not exist.")

                                            #Exercise 5 — Custom Exception

class InvalidAgeError(Exception):
    pass
try:
    age = int(input("Enter Your Age: "))

    if age < 18:
        raise InvalidAgeError("Age must be 18 or above.")
    print("Access Granted!")
except ValueError:
    print("Invalid input: Please enter a valid number for age.")



                                    #Project: Secure Student Age & Marks Validator

class InvalidAgeError(Exception):
    pass
try:
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    marks = float(input("Enter Marks: "))

    if age < 18:
        raise InvalidAgeError("Age must be 18 or older!")
    if marks < 0 or marks > 100:
        raise ValueError("marks must be Between 0 and 100.")
except ValueError as error:
    print(error)
except InvalidAgeError as error:
    print(error)
else:
    print("--- Student Information ---")
    print(f"Name: {name}\nAge: {age}\nMarks: {marks}")
finally:
    print("Program finished.")
"""

                                                #Practical Challenge

class InvalidAgeError(Exception):
    pass
try:
    age = int(input("Enter Age: "))
    if age < 18:
        raise InvalidAgeError("Age must be 18 or more")
except ValueError as error:
    print(error)
except InvalidAgeError as error:
    print(error)
else:
    print("Access Granted!")
finally:
    print("Program finished.")

