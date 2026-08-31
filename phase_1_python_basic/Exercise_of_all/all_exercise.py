"""count = 1

while count <=25:
    print(count)
    count += 1"""


"""count = 25

while count >=1:
    print(count)
    count -= 1"""

"""count = 2

while count <=30:
    print(count)

    count += 2"""

"""count = 1

while count <=25:
    print(count)
    count += 2"""

"""count = 100

while count >=10:
    print(count)
    count -= 10"""



"""number = int(input("Enter Your Number :"))
count = 1

while count <=15:
    print(number, "X", count, "=", number * count)
    count += 1"""


"""number = int(input("Enter Your Number :"))
count = 15

while count >=1:
    print(number, "X", count, "=", number * count)
    count -= 1"""




"""number = int(input("Enter Your Number :"))
count = 2

while count <=20:
    print(number, "X", count, "=", number * count)
    count += 2"""


"""correct_password = "AI2026"

password = ""

while password != correct_password:
    password = input("Enter Password :")
print("Access Granted")"""


"""correct_password = "Python@123"
password = ""

while password != correct_password:
    password = input("Enter Password :")

    if password != correct_password:
        print("Wrong Password! Try Again.")
print("Welcome!")"""


"""count = 1

while count <=20:
    print(count)
    if count ==14:
        break
    count +=1
"""


# p12 doubt explain this question in details

"""count =1

while count <= 20:
    print(count)
    if count % 5 ==0:
        continue
    count += 1"""


# # p13 also doubt explain this question in details

"""count = 1

while count <=20:
    print(count)
    if count %2 ==0:
        continue
    count += 1"""

# # p14 also doubt explain this question in details

"""number = int(input("Enter Your Number :"))

for i in range(1,11):
    print(number , "X", i, "=", number * i)"""




#p1
"""name = input("Enter Your Name :")
marks = int(input("Enter Your Marks :"))

if marks >=90:
    print("Excellent Student")
elif marks >=75:
    print("Grade A")
elif marks >=65:
    print("Grade B")
elif marks >= 35:
    print("Grade C")
else:
    print("Faill")"""


#p2
"""number = int(input("Enter Your Number :"))

if number % 2 == 0:
    print("Number Is Even")
else:
    print("Number is Odd")

if number > 0:
    print("Number Is Positive")
else:
    print("Number is Negative")"""



#p3
"""number = int(input('Enter Your Number :'))
count = 5
while count <=15:
    print(number, "X", count, "=", number * count)
    count += 1"""


#p4

"""total = 0
count = 25

while count <=75:
    total = total + count
    count += 1
print(total)"""

#p5

"""total = 0
count = 20

while count <=60:
    total = total + count
    count += 2
print(total)"""


#p6

"""correct_password = "Hardik123"
password = ""

while password != correct_password:
    password = input("Enter Your Password :")

    if password != correct_password:
        print("Wrong Password Please try again")
    
print("Welcome Buddy")"""


# p7 
"""count = 1

while count <=30:
    if count % 5 == 0:
        count +=1
        continue
    print(count)
    count += 1"""


#p8
"""number = int(input("Enter Number Between 1 to 20 :"))
count = 1

while count <=20:
    if count == number:
        break
    print(count)
    count += 1"""


"""number = int(input("Enter Number :"))
count = 2

while count <= number:
    if count % 2 == 0:
        print(count)
    count +=1"""


                        #=================================
                               #function day exersice 
                        #=================================


#1 STUDENT RESULT

"""def result(name,marks):
    if marks >=35:
        return name +" : Pass"
    else:
        return name + " : Fail"
print(result("Hardik",80))
print(result("Priya",21))"""

# #2 REVESE TABLE 

"""number = int(input("Enter Number :"))
count = 10

while count >=1:
    print(number, "X", count, "=", number * count)
    count -= 1"""

#3 sum of number using for loop

"""total = 0
for i in range(1,50):
    total = total + i
print(total)
"""

#password using while

"""correct_password = "Python2026"
password = ""

while password != correct_password:
    password = input("Enter Password :")

    if password != correct_password:
        print("Wrong Password")
print("Access Granted")"""

#largest number 

"""def largest(a,b):
    if a > b:
        return a
    else:
        return b
print(largest(9,4))"""

"""def dream(country="Germany"):
    print("My Dream Country is :", country)
dream()
dream("japan")
dream("Canada")

for i in range(1,21):
    if i % 3 ==0:
        continue
    print(i)"""

"""number = int(input("Enter Number bt 1 to 20 :"))
count = 1

while number <= 20:
    if count == number:
        break
    print(count)
    count += 1"""

"""def square(numebr):
    return numebr * numebr

result = square(8)
print(result)"""


"""def calculator(a,b):
    return a + b
answer = calculator(15,25)
print("Answer :", answer)"""


#1                  4/8/23

"""marks = int(input("Enter Your Marks :"))

if marks >= 75:
    print("Distinction")
elif  60<= marks <=74:
    print("First Class")
elif 35<= marks <=59:
    print("Second Class")
else:
    print("Fail")"""


#2

"""number = int(input("Enter Your Number :"))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else: 
    print("Zero")"""


#3
"""age = int(input("Enter Your Age :"))

if age >=20:
    print("Adult")
elif 13<= age <=19:
    print("Teenager")
else:
    print("Child")"""


#4
"""num1 = int(input("Enter Number 1:"))
num2 = int(input("Enter Number 2:"))

if num1 > num2:
    print(num1)
else:
    print(num2)"""

#5

"""year = int(input("Enter Your Year :"))

if year %2 == 0:
    print("Even Year")
else:
    print("Odd Year")"""

#6

"""for i in range(10,101,10):
    print(i)"""


#7

"""for i in range(51,100,2):
    print(i)"""

#8

"""number = int(input("Enter Number :"))

for i in range(3,16):
    print(number, "X", i, "=", number * i)"""

#9

"""total = 0

for i in range(50,101):
    total = total + i
print(total)"""


#10  

"""total = 0

for i in range(20,61,2):
    total = total + i
print(total)"""


#11             WHILE LOOP

"""count = 30
while count >=1:
    print(count)
    count -= 1"""

#12
"""number= int(input("Enter Number :"))
count = 15"""

"""while count >=5:
    print(number, "X", count, "=", number * count)
    count -= 1"""

#13

"""correct_password = "AIEngineer"
password = ""

while password != correct_password:
    password = input("Enter Pass:")

    if password != correct_password:
        print("Wrong Pass")
print("Welcome Buddy")"""

#14 

"""count =1

while count <=25:
    if count == 18:
        break
    print(count)
    count +=1"""

#15

"""count = 1

while count <=20:
    if count % 4 ==0:
        count +=1
        continue

    print(count)
    count +=1"""

#16

"""count = 50

while count <=100:
    if count ==75:
        break
    print(count)
    count += 1"""


#17      FUNCTION

"""def cube(number):
    return number ** 3
ans = cube(5)
print("Answer :",ans)"""

#18

"""def student(name,marks):
    if marks >=35:
        return name + " : Pass"
    else:
        return name + " : Fail"
print(student("Hardik", 99))
print(student("Priya", 21))"""


#19

"""def greeting(name="ChatGPT"):
    print("Hello", name)
greeting()"""


#20

"""def calculator(a,b):
    return a + b, a - b, a * b
result = calculator(10,5)
print("Ans :", result)"""



#1

"""marks = int(input("Enter Marks :"))

if marks >= 90:
    print("Exellent")
elif 75 <= marks <=89:
    print("Grade A")
elif 50<= marks <=74:
    print("Grade B")
else:
    print("Fail")"""
 

#2
"""number = int(input("Enter Number :"))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")"""

#3
"""for i in range(15,31):
    print(i)"""

#4
"""for i in range(1,26,2):
    print(i)"""

#5
"""num = int(input("Enter Number :"))
count =12
while count >=1:
    print(num , "X", count, "=", num * count)
    count -= 1"""

#6
"""correct_Pass = "PythonAI2026"
password = ""

while password != correct_Pass:
    password = input("Enter Pass :")

    if password != correct_Pass:
        print("Wrong Pass")
print("Welcome Dude")
"""
#7
"""count = 1
while count <=30:
    if count == 18:
        break
    print(count)
    count += 1"""

#8
"""count = 1
while count <= 20:
    if count % 4 == 0:
        count += 1
        continue
    print(count)
    count += 1"""


#9
"""def square(number):
    return number * number
result = square(4)
print(result)"""

#10
"""def eligible(age):
    if age >=18:
        return "Eligible"
    else:
        return "Not Eligible"
ans = eligible(14)
print(ans)"""

#11
"""def dream(country="Germany"):
    print("My Dream Country Is ", country)
dream()"""

#12
"""def calculator(a, b):
    return a +b, a - b, a * b
ans = calculator(10,5)
print(ans)"""

#13
"""fruits = ["Apple", "Banana", "Mango","Orange", "Grapes"]
print(fruits[0])
print(fruits[-1])"""

#14
"""marks = [70, 80, 90]
marks[1]= 85
print(marks)"""

#15
"""friends = ["Rahul", "Aman"]
friends.append("Hardik")
friends.append("Priya")
print(friends)"""

#16
"""numbers = [10, 30, 40]
numbers.insert(1,20)
print(numbers)
"""
#17
"""countries = ["India", "Germany", "Japan", "Canada"]
countries.remove("Germany")
print(countries)
#18
countries.pop(-1)
print(countries)"""


#19
"""num = [10,30,20,50,40]
num.sort()
print(num)

num.sort(reverse=True)
print(num)"""

#20
"""languages = ["Python", "Java", "C++", "JavaScript"]
languages.reverse()
print(languages)

print(len(languages))"""

# #21
"""def student(name, marks):
    if marks >35:
        return name + " : Pass"
    else:
        return name + " : Fail"
print(student("Hardik",99))
print(student("Priya",21))

students = ["Hardik", "Rahul", "Priya"]
print(students)

print(len(students))

students.append("Aman")
print(students)

students.reverse()
print(students)"""



                        #===========================
                            #NESTED LOOP EXERCISES
                        #===========================
#1
"""for i in range(1,6):
    for j in range(i):
        print("#", end=" ")
    print()"""

#2
"""for i in range(1, 6):
    for j in range(1, i + 1):
        print(j,end=" ")
    print()"""

#3
"""letters = ["A", "B", "C", "D"]
 
for i in range(1, 5):
    for j in range(i):
        print(letters[j], end=" ")
    print()
"""
#4
"""for i in range(1,6):
    for j in range(6 - i):
        print(i, end=" ")
    print()"""

#5
"""for i in range(1,6):
    for j in range(5, i -1, -1):
        print(j, end="")
    print()"""

#6
"""for i in range(0,4):
    for j in range(i,-1,-1):
        print(j, end="")
    print()"""

#7
"""letters = ["A", "B", "C", "D", "E"]

for i in range(0,5):
    for j in range(i + 1):
        print(letters[i], end=" ")
    print()"""

#8
"""for i in range(5,0,-1):
    for j in range(1,i + 1):
        print(j, end="")
    print()"""

#10
"""for i in range(1,6):
    for j in range(i, 0, -1):
        print(j, end="")
    print()"""





                                #1. Even or Odd
# # Take a number.
# # Check whether it is even or odd.

"""number = int(input("Enter Number :"))

if number % 2 == 0:
    print("Number Is Even")
else:
    print("Number is Odd")"""


#                             #2 Positive, Negative or Zero
# # Take a number.
# # Print whether it is positive, negative, or zero.

"""num = int(input("Enter Number :"))

if num > 0:
    print("Number Is Positive")
elif num < 0:
    print("Number is Negative")
else:
    print("Number is Zero")
"""

#                             #3 Largest of Three Numbers
# # Take 3 numbers.
# # Find the largest using conditions.

"""
num1 = int(input("Enter Number 1 :"))
num2 = int(input("Enter Number 2 :"))
num3 = int(input("Enter Number 3 :"))

if num1 and num2 < num3:
    print("Largest Number Is Number 3")
elif num3 and num2 <  num1:
    print("Largest is Number 1  ")
else:
    print("Largest Number Is Number 2:")
"""


                                #4 Simple Calculator

# Take two numbers and an operator + - * /.
# Perform the operation.
# Handle invalid input with try/except.

"""
try:

    num1 = int(input("Enter Number 1 :"))
    operator = input("Enter Operator (+, -, *, /) : ")
    num2 = int(input("Enter Number 2 :"))

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    else:
        print("Invalid Operators")
        result = None
    if result is not None:
        print("Answer :", result)
except ValueError:
    print("Invalid Number")
"""

                            #5 Temperature Converter

# Create a program that converts:

# Celsius → Fahrenheit
# Fahrenheit → Celsius
"""
print("Temperature Converter")
print("1. Calcius To Fahrenheit")
print("2. Fahrenheit To Calcius")

choice =input("Enter Your Choice 1 or 2 :")

if choice == "1":
    calcius = float(input("Enter Temperature In Calcius :"))
    fahrenheit = (calcius * 9/5) + 32

    print(calcius, ":", fahrenheit)
elif choice == "2":
    fahrenheit = float(input("Enter Temperature In Fahreneit :"))
    calcius = (fahrenheit - 32) * 5/9
    print(fahrenheit, ":", calcius)
else:
    print("Invalid Choice, Please select 1 or 2")
"""

                                #6. Multiplication Table
"""
number = int(input("Enter Your Number :"))
for i in range(1,11):
    print(number, "X", i, "=", number * i)
"""

                                    #7 Sum of Numbers
                                   
"""number = int(input("Enter Your Number :"))

total = 0
for i in range(1,number):
    total = total + i
    print("total =", total) """            
                                            #8. Factorial
"""                                 
number = int(input("Enter Your Number :"))

factorial = 1
for i in range(1, number + 1):
    factorial *= i
    print(factorial)
"""

                                        # 9. Count Digits

"""number = int(input("Enter Number :"))
num_digit = number
total = 0
for i in str(num_digit):
    num_digit = num_digit // 10
    total += 1
print(total)"""


                                        #10 Reverse a Number

"""number = int(input("Enter Number :"))

while number > 0:
    last_digit = number % 10
    print(last_digit, end="")
    number = number // 10"""

                                    #11 Count Vowels
"""
sentense = input("Enter Your String :")
vowels = "aeiou"
count = 0

for word in sentense:
    if word in vowels:
        count += 1
print("Vowel Count :",count)
"""

                                    #12 Reverse a String
"""
name =input("Enter Your Sentense :")
reverse_name = ""
for i in name:
    reverse_name = i + reverse_name
print(reverse_name)
"""
                                    #13 Palindrome Checker
"""
name = input("Enter Name :")    

reverse = ""
for i in name:
    reverse = i + reverse
print(reverse)

if name == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")
"""
                                    #14 — Character Counter

"""text = "hello"

count = {}

for char in text:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1
print(count)"""

                                #15 counts words

"""text = "I am learning Python"

words = text.split()
words_count = len(words)

print(words_count)
"""

                                #16 — Find Largest in List
"""
number = [12, 45, 23, 67, 34] 

max_number = 0
min_number = 100
for num in number:
    if num > max_number:
        max_number = num
    if num < min_number:
        min_number = num
print("Highest Number :", max_number)
print("Smallest Number :", min_number)
"""
                                #18 — Calculate List Sum
"""
number = [10, 20, 30, 40, 50]

lenght = number
lenght = len(number)
print(lenght)
"""
                                    #19 — Remove Duplicates

"""number = [1, 2, 2, 3, 4, 4, 5]

print(set(number))
"""
                                    #20 — Separate Even and Odd
"""
number = [10, 15, 22, 31, 44]   
even = 0
odd = 0
for num in number:
    if num % 2 == 0:
        print("Even Number :",num)
    else:
        print("Odd Numbers :",num)
"""

                                    #21 — Student Information [dictionaries]

"""student = {
    "name" : "Hardik",
    "age" : 24,
    "course" : "Python AI/ML"
}

for key,value, in student.items():
    print(key,":",value)
"""

                                    #22 Student Marks
"""students = {
    "python" : 85,
    "Math" : 75,
    "English" : 78
}


total = 0
max_marks = 0
min_marks = 100
for marks in students.values():
    if marks > max_marks:
        max_marks = marks
    if marks < min_marks:
        min_marks = marks
    total = total + marks
print(total)
print("Max Marks :",max_marks)
print("Min Marks :",min_marks)

avg = total / len(students)
print("Average :",avg)
"""

                                #23 — Word Frequency
"""contact = {}

def add_contact():
    name = input("Enter name: ")
    if not name:
        print("Name cannot be empty.")
        return

    phone = input("Enter phone number: ")
    contact[name] = phone
    print("Saved contact for", name)


def search_contact():
    name = input("Enter name to search: ")
    if name in contact:
        print(name, ":", contact[name])
    else:
        print("Contact not found.")


def delete_contact():
    name = input("Enter name to delete: ")
    if name in contact:
        del contact[name]
        print("Deleted contact:", name)
    else:
        print("Contact not found.")


def show_contact():
    if not contact:
        print("Your contact book is empty.")
        return

    print("Contacts:")
    for name, phone in sorted(contact.items()):
        print(name, ":", phone)


def main():
    while True:
        print("\n====== CONTACT BOOK ======")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. Show All Contacts")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            show_contact()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Please choose between 1 and 5.")
main()
"""

                                    #25 Number Analyzer

"""
num = int(input("Enter Your Number :"))
def analyze_number(num):
        return num
if num > 0:
    print("Positive Number")
elif num < 0:
    print("Negative Number")
else:
    print("Zero")

if num % 2 == 0:
        print("Even Number")
else:
         print("Odd Number")
found_divisor = None
for i in range(2,num):

    if num % i == 0:
        found_divisor = True
        break
if found_divisor:
    print("Not Prime Number")
else:
    print("Prime Number")
"""


                                #Exercise 1 — Number Analyzer
# Largest
# Smallest
# Total
# Average
# Even count
# Odd count
# Count numbers greater than 30
# Count numbers less than 20
"""
numbers = [18, 7, 42, 13, 56, 29, 8, 91]

print(max(numbers))
print(min(numbers))
print(sum(numbers))

avg = sum(numbers) / len(numbers)
print("Average :", avg)

even = 0
odd = 0
num_1 = 0
num_2 = 0
for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

    if num > 30:
        num_1 += 1
    if num < 20:
        num_2 += 1
print("Num > 30 :", num_1)
print("Num < 20 :", num_2)
print("Even Count :", even)
print("Odd Count :", odd)
"""

                                #Exercise 2 — String Analyzer
#Ask the user for a sentence.
# Total characters
# Total spaces
# Total words
# Number of "Python" occurrences
# Uppercase sentence
# Lowercase sentence
# First character
# Last character
# Whether it starts with "I"
# Whether it ends with "Python"                        
"""
sentence = input("Enter Your Sentence :")

print(len(sentence))
print(sentence.count(" "))

words_counts = len(sentence.split())
print(words_counts)

print(sentence.count("Python"))

print(sentence.upper())
print(sentence.lower())
print(sentence[0])
print(sentence[-1])
print(sentence.startswith("I"))
print(sentence.endswith("Python"))
"""
                                    #Exercise 3 — Student Dictionary
# Display All students
# Highest marks
# Lowest marks
# Average
# Pass count
# Fail count
# Search for a student
# Display searched student's grade

"""students = {
    "Hardik": 85,
    "Bhoomi": 92,
    "Neha": 38,
    "Rahul": 67,
    "Aman": 45
}

for key, value, in students.items():
    print(key, ":",value)
    if value >= 90:
        print(key,":",value,"Grade A")
    elif value >= 70:
            print(key,":",value,"Grade B")
    elif value >= 60:
        print(key,":",value,"Grade C")
    elif value >= 40:
        print(key,":",value,"Pass")
    else:
        print(key,":",value,"Fail !")

highest = 0
lowest = 100
pass_count = 0
fail_count = 0

for marks in students.values():
    if marks > highest:
        highest = marks
    if marks < lowest:
        lowest = marks
    
    if marks >= 40:
        pass_count += 1
    else:
        fail_count += 1
print("Pass Count :", pass_count)
print("Fail Count :", fail_count)
print("Highest Marks :",highest)
print("Lowest Marks :", lowest)

search = input("Search Student Name :")
if search in students:
    print(search,":",students[search])
"""

                                    #Exercise 4 — Tuple Explorer

# First country
# Last country
# Slice from index 1 to 3
# Find "Japan" index
# Check whether "Germany" exists
# Count total countries
"""
countries = ("India", "Germany", "Japan", "Canada", "France")

print(countries[0])
print(countries[-1])
print(countries[1:3])
print(countries.index("Japan"))
print(len(countries))
if "Germany" in countries:
    print("Exist")
else:
    print("Not Found")
"""

                                    #Exercise 5 — Set Manager

# Display unique numbers
# Add 60
# Remove 30
# Check whether 40 exists
# Display number of unique values
"""
numbers = {10, 20, 10, 30, 40, 20, 50}

print(len(numbers))
numbers.add(60)
numbers.remove(30)
if 40 in numbers:
    print("Exist")
else:
    print("Not Exist")
print(numbers)
"""

                                    #Exercise 6 — Positive/Negative Analyzer
# Positive count
# Negative count
# Zero count
# Even count
# Odd count
# Largest
# Smallest
# Average

"""
positve = 0
negative = 0
num = ""
even = 0
odd = 0
largest = float('-inf')
smallest = float('inf')
total = 0
count_input = 0
zero = 0
for num in range(1,11):
    num = int(input("Enter Number :"))
    count_input += 1
    if num > 0:
        positve += 1
    elif num < 0:
        negative += 1
    else:
        zero += 1

    if num % 2 == 0:
        even += 1
    else:
        odd += 1

    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
    total += num

    avg = total / count_input
print("Average :",avg)
print("Total :",total)
print("Zeros :",zero)
print("Largest Num :",largest)
print("Smallest Num :",smallest)

print("Even Count :", even)
print("Odd Count :",odd)  
print("Positve Count :",positve)
print("Negative Count :",negative)
"""


                                    #Exercise 7 — Password Validator
#Ask the user for a password.
# Minimum 8 characters
# Contains a digit
# Contains uppercase
# Contains lowercase
# Contains special character

"""password = input("Enter Password :")

has_lenght = False
has_digit = False
has_upper = False
has_lower = False
has_special = False

if len(password) <=8:
    has_lenght = True
    # print("Minimum 8 characters required !!")

for char in password:
    if char.isdigit():
        has_digit = True
    elif char.upper():
        has_upper = True
    elif char.lower():
        has_lower = True
    else:
        has_special = True


score = has_lenght + has_lower + has_digit + has_upper + has_special

if score == 5:
    clasification = "Strong"
elif score >= 3:
    clasification = "Medium"
else:
    clasification = "Weak"

print("length > = 8 :",has_lenght)
print("Contains Digit :",has_digit)
print("Contains UpperCase :",has_upper)
print("Contains LowerCase :", has_lower)
print("Contains Special Character :", has_special)
"""

                                    #Exercise 8 — Shopping Cart
"""
products = {
    "Laptop": 55000,
    "Mouse": 800,
    "Keyboard": 1500,
    "Monitor": 12000
}

product = input("Enter Product Name :")
quantity = int(input("Enter Quantity :"))
total = 0

if product in products:
    if quantity <= 0:
        print("Invalid Quantity Input!")
    else:
        total = products[product] * quantity
    print(products[product],"Total Price :", total)
else:
    print("Product Not Found!!")

"""
                                    #Exercise 9 — Word Analyzer

# Ask the user for a sentence.
# Number of words
# Longest word
# Shortest word
# Number of words beginning with "a"
# Number of words ending with "s"
# Number of vowels
# Number of consonants

"""sentence = input("Enter Your Sentence :")

words = sentence.split()
words_count = len(words)
print(words_count)

longest = max(words, key=len)
smallest = min(words, key=len)
print(longest)
print(smallest)


vowels = "aeiouAEIOU"
vowels_count = 0
consonants = 0

for char in sentence:
    if char in vowels:
        vowels_count += 1
    if char.isalpha() and char.lower() not in vowels:
        consonants += 1

print("Consonant Count :", consonants)
print("Vowels Count :", vowels_count)


start_a =0
end_s= 0
for word in words:
    if word.startswith("a"):
        start_a += 1
    if word.endswith("s"):
        end_s += 1
print("Start With A Count :", start_a)
print("End With S Count :", end_s)
"""
                            #Exercise 10 — Number Frequency 

#Find how many times each number occurs.
"""
numbers = [2, 5, 2, 8, 5, 2, 9, 8, 5, 2]
counts = {}
for num in numbers:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1
print(counts)
"""

                                #Exercise 11 — Number Function 
# Positive/negative/zero
# Even/odd
# Prime/not prime

"""def check(number):

    if number > 0:
        sign = "Positive"
    elif number < 0:
        sign = "Negative"
    else:
        sign = "Zero"
    
    if number % 2 == 0:
        parity = "Even Number"
    else:
        parity = "Odd Number"

    return number,sign, parity

print(check(12))
print(check(-7))
print(check(0))
"""


                            #Exercise 12 — List Statistics Function

# Maximum
# Minimum
# Total
# Average
# Even count
# Odd count
"""
def get_list(numbers):
    if not numbers:
        return {}
    
    total = sum(numbers)

    return {
        "Maximum": max(numbers),
        "Minimum": min(numbers),
        "Total": total,
        "Average": total / len(numbers),
        "even_count": sum(1 for x in numbers if int(x) % 2 == 0),
        "odd_count": sum(1 for x in numbers if int(x) % 2 != 0),

    }
data = [14,23,9,54,95,55]
stats = get_list(data)

for key, value, in stats.items():
    print(key, ":", value)
"""

                                #Exercise 13 — Student Grade Function

"""def calculate_grade(marks):

    if 90 <= marks <= 100:
        return "Grade A"
    elif 80 <= marks <=89:
        return "Grade B"
    elif 70 <= marks <= 79:
        return"Grade C"
    elif 60 <= marks <= 69:
        return "Grade D"
    elif 40 <= marks <= 59:
        return "Grade E"
    else:
        return "Fail"
    
print(calculate_grade(95))
print(calculate_grade(21))
print(calculate_grade(67))
print(calculate_grade(98))
print(calculate_grade(45))"""

                                    #Exercise 14 — Search Function

# Search for the student
# Return their marks if found
# Otherwise return a suitable result
"""
def search_student(students, name):

    if name in students:
        return students[name]
    else:
        return "Student Not Found"

students = {
    "Hardik": 85,
    "Bhoomi": 92,
    "Neha": 78,
    "Rahul": 67
}

print(search_student(students,"Hardik"))
print(search_student(students,"Bhoomi"))
print(search_student(students, "Anjali"))
"""

                                #Exercise 15 — Largest Without max()

# Find the largest number without using max()
# find_smallest without using min()
"""
def find_large_small(numbers):

    largest = float("-inf")
    smallest = float("inf")

    for num in numbers:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num

    return largest, smallest
numbers = [50, 41, 98, -21]
result = find_large_small(numbers)
print(result)
"""

                            #Exercise 16 — Student Management Console

# 1. Show Students
# 2. Add Student
# 3. Search Student
# 4. Show Highest
# 5. Show Lowest
# 6. Show Average
# 7. Show Pass/Fail Count
# 8. Exit
"""
students = {
    "Hardik": 85,
    "Bhoomi": 92,
    "Neha": 78,
    "Rahul": 67,
    "Vikram": 31
}

pass_marks = 40


def show_student():
    if not students:
        print("Student Not Found!")
        return

    print("\nStudents:")
    for name, marks in students.items():
        print(name, ":", marks)


def add_student():
    name = input("Add Student Name : ")

    if not name:
        print("Name Cannot Be Empty!")
        return

    try:
        marks = int(input("Enter Student Marks : "))

        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100.")
            return

        students[name] = marks
        print("Saved Info for :", name)

    except ValueError:
        print("Invalid Marks Input!")


def search_student():
    name = input("Enter Student Name : ")

    if name in students:
        print(name, ":", students[name])
    else:
        print("Student Not Found!!")


def show_highest():
    if not students:
        print("Student Not Found!!")
        return

    max_marks = max(students.values())

    print("Highest Scorer:")
    for name, marks in students.items():
        if marks == max_marks:
            print(name, ":", marks)


def show_lowest():
    if not students:
        print("Student Not Found!!")
        return

    min_marks = min(students.values())

    print("Lowest Scorer:")
    for name, marks in students.items():
        if marks == min_marks:
            print(name, ":", marks)


def show_average():
    if not students:
        print("Student Not Found!")
        return

    total_marks = sum(students.values())
    avg = total_marks / len(students)

    print("Total Students :", len(students))
    print("Average Marks :", avg)


def show_pass_fail():
    if not students:
        print("Student Not Found!!")
        return

    passed = sum(1 for marks in students.values() if marks >= pass_marks)
    failed = len(students) - passed

    print("Passed :", passed)
    print("Failed :", failed)


def main():
    while True:
        print("\n====== STUDENT MANAGEMENT SYSTEM ======")
        print("1. Show Students")
        print("2. Add Student")
        print("3. Search Student")
        print("4. Show Highest")
        print("5. Show Lowest")
        print("6. Show Average")
        print("7. Show Pass/Fail Count")
        print("8. Exit")

        choice = input("Enter Choice 1-8 : ")

        if choice == "1":
            show_student()

        elif choice == "2":
            add_student()

        elif choice == "3":
            search_student()

        elif choice == "4":
            show_highest()

        elif choice == "5":
            show_lowest()

        elif choice == "6":
            show_average()

        elif choice == "7":
            show_pass_fail()

        elif choice == "8":
            print("Exiting Student Management Console...")
            break

        else:
            print("Please enter a number from 1 to 8.")


if __name__ == "__main__":
    main()
 """  

                                    #Exercise 17 — ATM System 2.0
"""try:
    account = {
        "name": "Hardik",
        "PIN": 1137,
        "balance": 1400000
    }
    print("!!! WELCOME TO THE ATM !!! ")
    attempt = 0
    max_attempt = 3
    running = False
    while attempt < max_attempt:
        user_pin= int(input("Enter Your PIN :"))

        if account["PIN"] == user_pin:
            print("Welcome >>>",account["name"])
            running = True
            break
        else:
            attempt += 1
            remaining = max_attempt - attempt
            if remaining == 0:
                print("Access Denied")
            else:
                print("Invalid PIN!!!!")


    def check_balance():
        print("Current Balance :", account["balance"])
            
    def deposit():
        amount = int(input("Enter Deposit Amount :"))
        account["balance"] += amount
        print("Current Balance :", amount, "New Balance :", account["balance"])

    def withdraw_amount():
        withdraw_amount = int(input("Enter Withdraw Amount :"))

        if withdraw_amount <= account["balance"]:

            account["balance"] -= withdraw_amount
            print("Withdraw Amount", withdraw_amount, "Current Balance :", account["balance"])
        else:
            print("Insefficience Balance")

    while running:

        print("1. Check Balance.")
        print("2. Deposite")
        print("3. Withdraw")
        print("4. Exit!!")

        choice = input("Enter Your Choice :")

        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw_amount()
        elif choice == "4":
            print("Thank You For Using Our ATM!!!\n Have A Good Day!!")
            running = False
        else:
            print("Invalid Choice")


except ValueError:
    print("Invalid Input")"""

                                    #Exercise 18 — Advanced Calculator
"""try:
    def calculator(num1, operator, num2):

        if operator == "+":
            return num1 + num2
        elif operator == "-":
            return num1 - num2
        elif operator == "*":
            return num1 * num2
        elif operator == "/":
            return num1 / num2
        elif operator == "%":
            return num1 % num2
        elif operator == "**":
            return num1 ** num2
        else:
            print("Invalid Operator")

    while True:
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Power")
        print("7. Exit")

        choice = input("Enter Your Choice :")

        if choice == "1":
            operator = "+"
        elif choice == "2":
            operator = "-"
        elif choice == "3":
            operator = "*"
        elif choice == "4":
            operator = "/"
        elif choice == "5":
            operator = "%"
        elif choice == "6":
            operator = "**"
        elif choice == "7":
            print("Exiting")
            break
        else:
            print("Invalid Choice!")
            continue

        num1 = int(input("Enter Number 1 :"))
        num2 = int(input("Enter Number 2 :"))
        result = calculator(num1, operator, num2)
        print("Result :", result)
except ValueError:
    print("Invalid Number!")
except ZeroDivisionError:
    print("Cannot Divide By Zero!")"""

                            #Exercise 19 — Number Guessing Game 2.0
"""
import random
random_number = random.randint(1,100)
guess_number = ""
count = 0

print("<<<Choose Difficulty Level>>>")
print("1.Easy")
print("2.Medium")
print("3.Hard")

choice = input("Enter Your Choice :")

if choice == "1":
    max_attempt = 10
elif choice == "2":
    max_attempt = 7
elif choice == "3":
    max_attempt = 5
else:
    print("Invalid Choice")

while guess_number != random_number and count < max_attempt:
    guess_number = int(input("Guess Number Between 1 to 100 :"))
    count += 1        
    if guess_number > random_number:
        print("Too High!!")
    elif guess_number < random_number:
        print("Too Low")
        
if guess_number == random_number:
    print("Yeahhh!! Congrats You Win Buddy!!!")
else:
    print("Overconfidence detected!!!!")
    print("The number was:", random_number)
    
print(count, "attempts Completed")
"""

                            #Exercise 20 — Personal Expense Tracker
"""
expenses = [
    {
        "Expense Name": "Laptop",
        "Amount": 55000,
        "Category": "Electronics"
    },
    { 
        "Expense Name": "Food",
        "Amount": 400,
        "Category": "Food"
    },
    {
        "Expense Name": "Bus",
        "Amount": 80,
        "Category": "Travel"
    },
    {
        "Expense Name": "Book",
        "Amount": 550,
        "Category": "Education"
    }
]

for expense in expenses:
    print(expense["Expense Name"], ":", expense["Amount"], ":", expense["Category"])


name = input("Enter Expense Name :")
amount = int(input("Enter Expense Amount :"))
category = input("Enter Category of Expense :")

new_expense = {
    "Expense Name": name,
    "Amount": amount,
    "Category": category
}
expenses.append(new_expense)
total = 0
for expense in expenses:
    total = total + expense["Amount"]
print("Total Expense Amount :", total)

highest = float("-inf")
highest_expense = None
lowest = float("inf")
lowest_expense = None
total = 0
for expense in expenses:
    if expense["Amount"] > highest:
        highest = expense["Amount"]
        highest_expense = expense

    if expense["Amount"] < lowest:
        lowest = expense["Amount"]
        lowest_expense = expense
    
    total += expense["Amount"]
    avg = total / len(expenses)
print("Average :", avg)
print("Highest :", highest_expense["Expense Name"], highest)
print("lowest :",lowest_expense["Expense Name"],lowest)

search = input("Enter Expense Name :")
found = False
for expense in expenses:
    if search == expense["Expense Name"]:
        found = True
        print(expense["Expense Name"], ":", expense["Amount"], ":", expense["Category"])
if not found:
    print("Expense Not Found!!")

category_totals = {}

for expense in expenses:
    category = expense["Category"]
    amount = expense["Amount"]

    if category in category_totals:
        category_totals[category] += amount
    else:
        category_totals[category] = amount

for category, amount in category_totals.items():
    print(category, ":", amount)
"""


#Exercise 1 — Number Analyzer

num1 = int(input("Enter Number 1 :"))
num2 = int(input("Enter Number 2 :"))
num3 = int(input("Enter Number 3 :"))

num = [num1, num2, num3]

print(sum(num))
print(max(num))
print(min(num))

#Exercise 2 — String Check

sentense = input("Enter Sentense :")

words = sentense.split()
total_words = len(words)

vowels = "AEIOUaeiou"
vowels_count = 0
for char in sentense:
    if char in vowels:
        vowels_count += 1
print("Vowels Count :", vowels_count)
print(sentense.upper())
print("total Words :",total_words)


#Exercise 3 — List Check

numbers = [12, 7, 20, 5, 18, 9]

even = 0
odd = 0
total = 0
for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
    
    total = sum(numbers)
    average = total / len(numbers)

print("Even Count :", even)
print("Odd Count :", odd)
print("Total :", total)
print("Average :", average)


#Exercise 4 — Student Result

students = {
    "Hardik": 85,
    "Bhoomi": 35,
    "Rahul": 67
}

pass_marks = 40

for name, marks in students.items():
    if marks >= pass_marks:
        print(name,":", marks,":","Pass")
    else:
        print(name,":", marks,":","Fail")


#Exercise 5 — Safe Division

try:
    num1 = int(input("Enter Number 1 :"))
    num2 = int(input("Enter Number 2 :"))

    result = num1 / num2
    print("Result :", result)
except ValueError:
    print("Invalid Input")
except ZeroDivisionError:
    print("cannot divide by Zero")