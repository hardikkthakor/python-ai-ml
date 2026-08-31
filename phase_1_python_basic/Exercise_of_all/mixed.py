



                            #1======================
                                # Highest mark
                                # Lowest mark
                                # Total
                                # Average
                            #1======================

"""marks = [75, 80, 95, 60, 85]
print(max(marks))
print(min(marks))
print(sum(marks))

average = sum(marks) / len(marks)

print("Average = ", average)"""


#                             #2=====================================
#                                     # First country
#                                     # Last country
#                                     # Total countries
#                                     # Slice only the middle two countries
#                             #2=====================================

"""countries = ("India", "Germany", "Japan", "Canada")

print(countries[0])
print(countries[-1])
print(len(countries))
print(countries[1:3])
"""

#                             #3=====================================
#                                     # Total unique numbers
#                                     # Add 50
#                                     # Remove 20 using discard()
#                                     # Print final set
#                             #3=====================================
                        
"""numbers = {10,20,30,20,40,10}

print(numbers)
numbers.add(50)
numbers.discard(20)
print(numbers)"""

#                             #4=====================================
#                                         # Even numbers
#                                         # Odd numbers
#                             #4=====================================

"""numbers = [10,15,20,25,30,35]


even_count = 0
odd_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Even Count =", even_count)
print("Odd_Count = ",odd_count)"""


#                             #5=====================================
#                                        #FOUND NOT FOUND
#                             #5=====================================

"""fruits = ["Apple","Banana","Mango","Orange"]

if "Mango" in fruits:
    print("Found")
else:
    print("Not Found")"""

#                             #6=====================================
#                                     # How many Blue
#                                     # Index of Green                                      
#                             #6=====================================

"""colors = ("Red","Blue","Green","Blue")
print(colors.count("Blue"))
print(colors.index("Green"))"""


#                             #7=====================================
                                     
#                             #7=====================================

"""students = {
    "Hardik",
    "Rahul",
    "Priya"
}

for student in students:
    print("Welcome ", student)"""

#                             #8=====================================
                                       
#                             #8=====================================

"""numbers = [10,20,30,40,50]

for num in numbers:
    if num % 2 == 0:
        print(num, "Is Even")"""

#                             #9=====================================
#                                        #FUNCTION
#                             #9=====================================
"""def greet(name):
    print("Welcome ", name)

greet("Hardik")"""


#                                             #10
"""def findLargest(numbers):
    return max(numbers)

result = findLargest([50,80,20,100])
print(result)"""


#                             #9=====================================
#                             # ALL IN ONE
#                                         # Largest Number
#                                         # Smallest Number
#                                         # Total
#                                         # Average
#                                         # Even Count
#                                         # Odd Count
#                             #9=====================================

"""numbers = [10,20,30,40,50]
print(max(numbers))
print(min(numbers))
print(sum(numbers))

Avg = sum(numbers) / len(numbers)
print("Average =", Avg)

even_count = 0
odd_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Even Count =", even_count)
print("Odd Count =", odd_count)"""



#1
# Largest number
# Smallest number
# Total
# Averag

"""numbers = [12, 25, 18, 40, 33]
print(max(numbers))
print(min(numbers))
print(sum(numbers))

average = sum(numbers) / len(numbers)
print("Average = ", average)
"""

# #2
# # First city
# # Last city
# # Total cities
# # Middle three cities

"""cities = ("Ahmedabad", "Berlin", "Tokyo", "Paris", "London")
print(cities[0])
print(cities[-1])
print(len(cities))
print(cities[1:4])
"""
# #3
# # Total unique numbers
# # Add 60
# # Remove 30
# # Print the final set

"""numbers = {10, 20, 10, 30, 40, 20, 50}
print(len(numbers))
numbers.add(60)
numbers.discard(30)
print(numbers)
"""

# #4
# # Even numbers
# # Odd numbers
"""
numbers = [5, 10, 15, 20, 25, 30]
even = 0
odd = 0
for num in numbers:
    if num % 2 == 0:
        even += 1
    else: 
        odd += 1
print("Even Num :", even)
print("Odd Num :", odd)
"""
# #5
# # How many students passed (>=40)
# # How many students failed (<40)
"""
marks = [35, 70, 90, 25, 80]

pass_count = 0
fail_count = 0
for mark in marks:
    if mark >=40:
        pass_count += 1
    else:
        fail_count += 1
print("Pass :", pass_count)
print("Fail :", fail_count)"""

# #6
# #FOUND NOT FOUND

"""names = ["Hardik", "Rahul", "Priya", "Aman"]

if "Priya" in names:
    print("Found")
else:
    print("Not Found")
"""
# #7
"""def square(num):
    return num * num

result = square(6)

print("Ans =", result)"""

# #8
"""def isEven(num):
    
    if num % 2 ==0:
        return True
    else:
        return False

result = isEven(9)
print(result)"""

# #9
"""def findSmallest(numbers):
    return findSmallest

num = [10,9,11,15,19,25]
print(min(num))
"""
# #10
"""numbers = [10, 15, 20, 25, 30]

for num in numbers:

    if num % 2 == 0:
        print(num, "Is Even")
    else:
        print(num,"Is Odd")"""

# #11
# How many times "Blue" appears
# Index of "Green"
# Last three colors using slicing

"""colors = ("Red", "Blue", "Green", "Blue", "Yellow")

print(colors.count("Blue"))
print(colors.index("Green"))
print(colors[2:])"""

# #12
"""languages = {"Python", "Java"}

languages.add("C++")
languages.add("JavaScript")
languages.remove("Java")
print(languages)"""

# #13
# # Largest
# # Smallest
# # Total
# # Average
# # Even Count
# # Odd Count
# # Passed numbers (>=20)
# # Failed numbers (<20)

"""numbers = [22, 15, 40, 13, 18, 50, 9]

print(max(numbers))
print(min(numbers))
print(sum(numbers))

avg = sum(numbers) / len(numbers)
print("Average =",avg)

even = 0
odd = 0
for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even Count =", even)
print("Odd Count =", odd)

pass_numbers = 0
fail_numbers = 0

for n in numbers:
    if n >=20:
        pass_numbers += 1
    else:
        fail_numbers += 1

print("Pass Count = ",pass_numbers)
print("Fail Count =", fail_numbers)"""


# #14  -- USING ONLY ONE LOOP 
# # Total
# # Average
# # Largest
# # Smallest

"""numbers = [10, 20, 30, 40, 50]
total = 0
average = 0
min_num = numbers[0]
max_num = numbers[0]
for num in numbers:
    total =total + num
    average = total / len(numbers)

    if num < min_num:
        min_num = num

    if num > max_num:
        max_num = num

print(total)
print(average)
print(max_num)
print(min_num)"""



# #1
"""numbers = [12, 7, 18, 25, 30, 9]
print(len(numbers))
print(max(numbers))
print(min(numbers))

even = 0
odd = 0
for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even Count =", even)
print("Odd Count =", odd)"""

# #2
"""movies = ("Interstellar", "Inception", "Avatar", "Titanic", "Joker")
print(movies[0])
print(movies[-1])
print(len(movies))
print(movies[1:4])
print(movies.index("Avatar"))"""

# #3
"""fruits = {"Apple", "Banana", "Apple", "Mango", "Orange", "Banana"}

print(len(fruits))
fruits.add("Grapes")
fruits.discard("Mango")

if "Apple" in fruits:
    print("Exist")
else:
    print("Not Exist")

for fruit in fruits: #you said loop through so thats why i print like this
    print(fruit)"""

# #4
"""def findAverage(numbers):
    return average(numbers)

num = [10, 20, 30, 40, 50]
print(sum(num))

average = sum(num) / len(num)

print("Average =", average)
"""
# #5
"""marks = [85, 35, 70, 25, 95, 40]

pass_count = 0
fail_count = 0
for mark in marks:
    if mark >= 40:
        pass_count += 1
    else:
        fail_count += 1
print("Pass =", pass_count)
print("Fail =", fail_count)

print(max(marks))
print(min(marks))
avg = sum(marks) / len(marks)

print("Average = ", avg)
"""

# #6
"""numbers = [25, 18, 42, 11, 60, 9]

max_num = numbers[0]
min_num = numbers[0]
total = 0
avg = 0
for num in numbers:
    total = total + num
    if num < min_num:
        min_num = num

    if num > max_num:
        max_num = num

        avg = total / len(numbers)

print(max_num)
print(min_num)
print(total)
print("Average = ", avg)"""



                            #1 — List + Loop + Condition
# Print every even number
# Print every odd number
# Count even numbers
# Count odd numbers

"""numbers = [12, 7, 20, 15, 30, 9, 40]

even = 0
odd = 0
for num in numbers:
    if num % 2 ==0:
        even += 1
        print("Even Number :",num)
    else:
        odd += 1
        print("Odd Number :",num)
print("Even Count =", even)
print("Odd Count =",odd)"""

                                #2— List Statistics
# Find largest
# Find smallest
# Find total
# Find average
# Count marks >= 40
# Count marks < 40

"""marks = [75, 82, 45, 91, 63, 38, 55]

print(max(marks))
print(min(marks))
print(sum(marks))

avg = sum(marks) / len(marks)
print("Average =",avg)

count_1=0
count_2=0

for mark in marks:
    if mark >=40:
        count_1 +=1
    else:
        count_2 +=1

print("Marks >=40 ->",count_1)
print("Marks <40 ->", count_2)
"""

                            #3 — Tuple + String Methods
# Print first country
# Print last country
# Print middle three countries
# Find the index of "Japan"
# Check whether "Germany" exists

"""countries = ("India", "Germany", "Japan", "Canada", "France")
print(countries[0])
print(countries[-1])
print(countries[1:4])
print(countries.index("Japan"))

if "Germany" in countries:
    print("Exist")
else:
    print("Not Exist")"""
   
                            #4 — Set Practice
# Print total unique numbers
# Add 60
# Remove 30 using discard()
# Check whether 40 exists
# Print the final set
                          
"""numbers = {10, 20, 10, 30, 40, 20, 50}

print(len(numbers))
numbers.add(60)
numbers.discard(30)
if 40 in numbers:
    print("Exist")
else:
    print("Not Exist")

print(numbers)"""

                                #5 — Dictionary Practice
# Print name
# Print dream
# Change country to "Canada"
# Add "language": "Python"
# Remove age
# Print every key and value

"""student = {
    "name": "Hardik",
    "age": 24,
    "country": "Germany",
    "dream": "AI Engineer"
}

print(student["name"])
print(student["dream"])

student["country"] = "Canada"
student.pop("age")

for key, value, in student.items():
    print(key, "=", value)"""

                                #6 — String + List
# Count "Python"
# Check if it starts with "Python"
# Check if it ends with "language"
# Split the sentence
# Print the first word
# Print the last word
                                
"""sentence = "Python is my favorite language"
print(sentence.count("python"))

print(sentence.startswith("Python"))
print(sentence.endswith("language"))
print(sentence.split())
print(sentence[0])
print(sentence[-1])"""

        
                                    #7 — Function + Condition
"""def is_pass(marks):
        if marks >= 40:
            return True
        else:
            return False

print(is_pass(75))
print(is_pass(35))
"""

                                    #8 — Function + List
"""def find_largest(numbers):

    largest = numbers[0]

    for num in numbers:
            if num > largest:
                largest = num
    return largest

numbers = [25, 10, 90, 45, 60]
Result = find_largest(numbers)
print("The Largest Number Is =",Result)"""

                                    #9 — Mixed Challenge
# Find total
# Find average
# Find largest
# Find smallest
# Count even numbers
# Count odd numbers
# Count numbers >= 20
# Count numbers < 20  
                                  
"""numbers = [15, 22, 8, 35, 40, 11, 50]
even = 0
odd = 0
print(sum(numbers))

average = sum(numbers) / len(numbers)
print("Average =",average)

print(min(numbers))
print(max(numbers))

for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even Count =", even)
print("Odd Count =", odd)
num_1 = 0
num_2 = 0
for num in numbers:
    if num >= 20:
        num_1 += 1
    else:
        num_2 += 1
print("Number >= 20 =>",num_1)
print("Number < 20 =>",num_2)"""
                                        #10

# Print every student's name and mark.
# Count how many students passed (>= 40).
# Count how many failed (< 40).
# Find the highest mark.
# Find the lowest mark.
# Calculate the average mark.

"""students = {
    "Hardik": 85,
    "Rahul": 35,
    "Priya": 92,
    "Aman": 45,
    "Neha": 28
}

print(students)
pass_count =0
fail_count = 0
for marks in students.values():
    if marks >= 40:
        pass_count += 1
    else:
        fail_count += 1
print("Pass Count =", pass_count)
print("Fail Count =", fail_count)

max_marks = 0
min_marks = 100
for key, value in students.items():
    if value > max_marks:
        max_marks = value
    if value < min_marks:
        min_marks = value
print(max_marks)
print(min_marks)

total_marks = 0

for mark in students.values():
    total_marks += mark

average = total_marks / len(students)
print("Average Marks =",average)"""




                                    #1 — Number Analyzer
# Largest number
# Smallest number
# Total
# Average
# Even count
# Odd count
# How many numbers are >= 20
# How many numbers are < 20

"""numbers = [12, 45, 7, 30, 18, 55, 9]

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
       
    if num >= 20:  
        num_1 += 1
    else:
        num_2 +=1

print("Even Count :",even)
print("Odd Count :",odd)
print("Number >=20 :", num_1)
print("Number < 20 :",num_2)"""



# #                                     #2 — Student Search
"""students = {
    "Hardik": 85,
    "Rahul": 35,
    "Priya": 92,
    "Aman": 45
}

user = input("Enter Student Name :")

if user in students:
    print(user,":",students[user])
else:
    print("Student Not Found")


                                    #3 — Word Analyzer
# Total characters
# Number of spaces
# Number of words
# Number of times "Python" appears
# Sentence in uppercase
# Sentence in lowercase

sentence = input("Enter Your Sentence :")

print(len(sentence))
print(sentence.count(" "))
print(sentence.count("Python"))
print(sentence.upper())
print(sentence.lower())
print(sentence.startswith("I"))
"""

#                                     # 4 — Safe Calculator Function

# # Invalid number
# # Division by zero
# # Invalid operator
"""try:
    number_1 = int(input("Enter Number 1:"))
    operators = input("Enter Operators (+, -, *, /) :")
    number_2 = int(input("Enter Number 2: "))

    if operators == "+":
        result = number_1 + number_2
    elif operators == "-":
        result = number_1 - number_2
    elif operators == "*":
        result = number_1 * number_2
    elif operators == "/":
        result = number_1 / number_2
    else:
        print("Invalid Operator")
        result = None
    if result is not None:
        print("Answer :", result)
except ValueError:
    print("Invalid Input")
except ZeroDivisionError:
    print("Cannot Divide By Zero")"""



                                    #5 — Mini Student System


"""try:
    students = {
        "Hardik" : 85,
        "Rahul" : 35,
        "Priya" : 92,
        "Aman" : 45
    }

    max_marks = 0
    min_marks = 100

    for key,value, in students.items():
        if value > max_marks:
            max_marks = value
        if value < min_marks: 
            min_marks = value

    print("Highest Marks :",max_marks)
    print("Lowest Marks :",min_marks)

    total = sum(students.values())
    print("Total :",total)

    avg = total / len(students)
    print("Average :", avg)

    pass_count = 0
    fail_count = 0

    for marks in students.values():
        if marks >= 40:
            pass_count += 1
        else:
            fail_count += 1
    print("Pass Count :",pass_count)
    print("Fail Count :", fail_count)

    search = input("Enter Student Name :")

    if search in students:
        print(search, ":", students[search])
    else:
        print("Student Not Found !!")

    for key,marks, in students.items():
        if 90<= marks <=100:
            print(key,":",marks,"Grade A")
        elif 80 <= marks <= 89:
            print(key,":",marks,"Grade B")
        elif 70 <= marks <= 79:
            print(key,":",marks,"Grade C")
        elif 60 <= marks <= 69:
            print(key,":",marks,"Grade D")
        elif 40 <= marks <= 59:
            print(key,":",marks,"Grade E")
        else:
            print(key,":",marks,"Fail")

except ValueError:
    print("Invalid Input") """
 

#===============================
#Largest
# Smallest
# Average
# Even count
# Odd count

"""numbers = [15, 8, 42, 23, 10, 37]

largest = 0
smallest = 100
even = 0
odd = 0
total = 0
for num in numbers:
    total = total + num
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
    
print("Largest Number :",largest)
print("Smallest Number :",smallest)
print("Even Count :",even)
print("Odd Count :",odd)
print("total :", total)

avg = total / len(numbers)
print("Average :", avg)
"""


#========================================================================
# Display every student and their marks.
# Count passed students (>= 40).
# Count failed students (< 40).
# Find the highest marks.
# Ask the user for a student name.
# If found → display their marks.
# If not found → "Student Not Found".
# Display each student's grade.
#========================================================================

"""students = {
    "Hardik": 99,
    "Bhoomi": 65,
    "Neha" : 78,
    "Divyesh": 45,
    "Vishal": 21
}
max_marks = 0
for key,marks , in students.items():
    print(key,":", marks)
    
    if 90<= marks <=100:
        print(key,":",marks,"Grade A")
    elif 80 <= marks <= 89:
        print(key,":",marks,"Grade B")
    elif 70 <= marks <= 79:
        print(key,":",marks,"Grade C")
    elif 60 <= marks <= 69:
        print(key,":",marks,"Grade D")
    elif 40 <= marks <= 59:
        print(key,":",marks,"Grade E")
    else:
        print(key,":",marks,"Fail")

    if marks > max_marks:
        max_marks = marks
print("Highest Marks :", max_marks)

pass_count = 0
fail_count = 0
for marks in students.values():
    if marks >= 40:
        pass_count +=1
    else:
        fail_count += 1
print("Pass Count :",pass_count)
print("Fail Count :",fail_count)


user = input("Enter Student Name :")
if user in students:
    print(user,":", students[user])
else:
    print("Student Not Found")"""



                                    #Exercise 1 — Number Analyzer

# Largest
# Smallest
# Total
# Average
# Even numbers
# Odd numbers
# Even count
# Odd count
# Numbers greater than 30
"""numbers = [18, 7, 42, 13, 56, 29, 8, 91]

max_number = 0
min_number = 100
total = 0
even = 0
odd = 0
greater_num = 0
for num in numbers:
    if num > max_number:
        max_number = num
    if num < min_number:
        min_number = num
    total = total + num
    avg = total / len(numbers)


    if num % 2 == 0:
        even += 1
    else:
        odd += 1

    if num > 30:
        print(num)
print("Even Count :",even)
print("Odd Count :", odd)
print("Average :", avg)
print("Total :",total)
print("Highest Number :",max_number)
print("Smallest Number :",min_number)
"""

                            #Exercise 2 — String Analyzer

# Total characters
# Total spaces
# Total words
# Number of "Python" occurrences
# Uppercase sentence
# Lowercase sentence
# First character
# Last character
# Whether the sentence starts with "I"
# Whether it ends with "Python"
"""
char = input("Enter Your Characters :")

print(len(char))
print(char.count(" "))

words = char.split()
word_count = len(words)
print(word_count)

print("Python".count("python"))
print(char.upper())
print(char.lower())
print(char[0])
print(char[-1])
print(char.find("P"))
print(char.endswith("Python"))
"""

                                    #Exercise 3 — Student Dictionary
# Display all students and marks.
# Find highest marks.
# Find lowest marks.
# Calculate average.
# Count pass/fail.
# Search for a student.
# Display their grade.

"""students = {
    "Hardik": 85,
    "Bhoomi": 92,
    "Neha": 38,
    "Rahul": 67,
    "Aman": 45
}


for key, marks, in students.items():
    print(key, ":", marks)
    if 90<= marks <=100:
        print(key,":",marks,"Grade A")
    elif 80 <= marks <= 89:
        print(key,":",marks,"Grade B")
    elif 70 <= marks <= 79:
        print(key,":",marks,"Grade C")
    elif 60 <= marks <= 69:
        print(key,":",marks,"Grade D")
    elif 40 <= marks <= 59:
        print(key,":",marks,"Grade E")
    else:
        print(key,":",marks,"Fail")

total = 0
max_marks = 0
min_marks = 100
pass_count = 0
fail_count = 0
for marks in students.values():
    if marks > max_marks:
        max_marks = marks
    if marks < min_marks:
        min_marks = marks
    total = total + marks
    avg = total / len(students)

    if marks >= 40:
        pass_count += 1
    else:
        fail_count += 1
print("Pass Count :",pass_count)
print("Fail Count :", fail_count)
print("Average :",avg)
print("Maximum Marks :",max_marks)
print("Minimum Marks :", min_marks)

search = input("Enter Search Name :")
if search in students:
    print(search,":", students[search])
"""

                            #Exercise 4 — Safe Calculator
"""try:
    num1 = int(input("Enter Number 1 :"))
    operator = input("Enter Operator (*, -, /, +) :")
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
        print("Please Select Valid Operator")
        result = None
    if result is not None:
        print("Result :", result)

except ValueError:
    print("Invalid Input")
except ZeroDivisionError:
    print("Cannot Divided By Zero")
"""
                                #Exercise 5 — ATM Challenge 
# PIN verification
# Maximum 3 PIN attempts
# Check balance
# Deposit
# Withdraw
# Insufficient balance
# Exit
# Invalid menu choice
# Invalid numeric input                               
"""try:
    account = {
        "name": "Hardik",
        "PIN": 1137,
        "balance": 140000
    }
    attempt = 0
    max_attempts = 3
    running = False

    while attempt < max_attempts:
        user_pin = int(input("Enter Your PIN :"))

        if user_pin == account["PIN"]:
            print("Welcome", account["name"])
            running = True
            break
        else:
            attempt += 1
            remaining = max_attempts - attempt

            if max_attempts == attempt:
                print("Access Denied")
            else:
                print("Invalid PIN")

    while running is True:
        print("====== ATM MENU========")
        print("1.Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter Your Choice :")

        if choice == "1":
            print("Current Balance :", account["balance"])

        elif choice == "2":
            amount = int(input("Enter Deposite Amount :"))
            account["balance"] += amount
            print("Your Balance :",amount, "New Balance :", account["balance"])

        elif choice == "3":
            with_amount = int(input("Enter withdraw amount :"))
            if with_amount <= account["balance"]:
                account["balance"] -= with_amount
                print("Your Balance :", with_amount, "Available Balance :", account["balance"])
            else:
                print("Insufficient balance")
        elif choice == "4":
            print("Thank Your Choosing ATM")
            running = False
        else:
            print("Invalid Choice")
except ValueError:
    print("Invalid Input")
    """


                                #Exercise 6 — Mixed Boss Challenge

# Display all products.
# Find the cheapest product.
# Find the most expensive product.
# Calculate total price.
# Calculate average price.
# Ask the user for a product name.
# Show its price if found.
# Otherwise show "Product Not Found".
# Ask the user for a quantity.
# Calculate: price × quantity
"""try:
    products = {
        "Laptop": 55000,
        "Mouse": 800,
        "Keyboard": 1500,
        "Monitor": 12000,
        "Headphones": 2500
    }
    expensive_product = None
    cheapest_product = None                           
    max_amount = 0
    min_amount = 1000000
    total = 0
    for key, amount, in products.items():
        print(key, ":", amount)

        if amount > max_amount:
            max_amount = amount
            expensive_product = key
        if amount < min_amount:
            min_amount = amount
            cheapest_product = key
        total += amount
    print("Total Items Value :",total)
    print("expensive product :",expensive_product, max_amount)
    print("cheapest product is :",cheapest_product, min_amount)

    avg = total / len(products)
    print("Average :", avg)

    product = input("Enter Product Name :")
    quantity = int(input("Enter Quantity :"))

    if product in products:
        print(product, ":", products[product])
        quantity *= products[product] 
    else:
        print("Product Not Found")
    print("Total Price :", quantity)
except ValueError:
    print("Invalid Input")"""



                                    #Question 1 — Numbers + Loop + Conditions
"""
numbers = []

for i in range(5):
    num = int(input("Enter Number :"))
    numbers.append(num)

total = 0
even_count = 0
odd_count = 0

for num in numbers:
    total += num

    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

average = total / len(numbers)

print("Total :", total)
print("Average :", average)
print("Even Count :", even_count)
print("Odd Count :", odd_count)
"""
                                #Question 2 — Function + Condition
"""
def check_number(number):
    if number > 0:
        if number  % 2 == 0:
            return "Postive Even"
        else:
            return "Positive Odd"
    elif number < 0:
        if number % 2 == 0:
            return "Negative Even"
        else:
            return "Negative Odd"
    else:
        return "Zero"
print(check_number(10))
print(check_number(-7))
print(check_number(-8))
print(check_number(5))
print(check_number(0))
"""
                                #Question 3 — List + Loop
"""
numbers = [12, 7, 20, 5, 18, 9]

print(sum(numbers))
print(max(numbers))
print(min(numbers))

even = 0
odd = 0

for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even Count :", even)
print("Odd Count :", odd)

                                    #Question 4 — String Basics

sentence = input("Enter Sentence :")

print(len(sentence))

words = sentence.split()
word_count = len(words)
print(word_count)

print(sentence.upper())
print(sentence.lower())

vowels = "aeiouAEIOU"
vowels_count = 0
consonant = 0

for char in sentence:
    if char in vowels:
        vowels_count += 1
    elif char.isalpha():
        consonant += 1
print("Vowels Count :", vowels_count)
print("Consonant Count :", consonant)
"""

                                        #Question 5 — Dictionary + Function

"""def search_student(students, name):
    if name in students:
        return students[name]
    else:
        return "Student Not Found!!"

students = {
    "Hardik": 85,
    "Bhoomi": 92,
    "Neha": 78,
    "Rahul": 67
}

print(search_student(students, "Hardik"))
print(search_student(students,"Rahul"))
print(search_student(students, "Anjali"))"""

                                        #Question 6 — Tuple + Set
"""
colors = ("Red", "Blue", "Green", "Yellow")

print(colors[0])
print(colors[-1])
print(len(colors))

numbers = [10, 20, 10, 30, 20, 40, 30]

unique = set(numbers)
print(len(unique))
"""

                                    #Question 7 — Exception Handling
"""try:
    num1 = int(input("Enter number 1 :"))
    num2 = int(input("Enter Number 2 :"))

    result = num1 / num2
    print("Result :", result)
except ValueError:
    print("Invalid Input")
except ZeroDivisionError:
    print("Cannot Divide by zero")
"""

                                        #Question 8 — Functions + Lists
"""
def analyze_number(numbers):


    maximum = float("-inf")
    minimum = float("inf")
    total = 0
    for num in numbers:
        if num > maximum:
            maximum = num
        elif num < minimum:
            minimum = num  
        total += num
    return maximum, minimum,total

numbers = [10, 15, 20, 7, 8]
result = analyze_number(numbers)
print("Result :", result)
"""

                        #Question 9 — String + Loop + Condition
"""
sentence = input("Enter Sentence :")

vowels = "aeiouAEIOU"
vowels_count = 0
constants = 0
space = 0
for char in sentence:
    if char in vowels:
        vowels_count += 1
    elif char.isalpha():
        constants += 1
    elif char == " ":
        space += 1

print("Vowels Count :", vowels_count)
print("Constants :", constants)
print("Spaces :", space)
"""

                                #Question 10 — Final Basic Revision
"""
students = {
    "Hardik": 85,
    "Bhoomi": 92,
    "Neha": 78,
    "Rahul": 67
}

pass_marks = 40

def show_result(students):
    for name, marks in students.items():
        if marks >= pass_marks:
            print(name,":",marks, "Pass")
        else:
            print(name,":",marks, "Fail")
show_result(students)
"""

                                    #Final Test — Question 1

"""number = []
total = 0
smalest = float("inf")
largest = float("-inf")
even = 0
odd = 0
for i in range(5):
    number = int(input("Enter Number :"))

    if number > largest:
        largest = number
    if number < smalest:
        smalest = number
    if number % 2 == 0:
        even += 1
    else:
        odd += 1
    total += number
    avg = total / 5
print("average :", avg)
print("Largest :", largest)
print("Smalest :", smalest)
print("Even :", even)
print("Odd :", odd)
print("Total :", total)
"""

                                    #Final Test — Question 2

"""def check_number(number):
    if number > 0:
        if number % 2 == 0:
            return "Positive Even"
        else:
            return "Positive Odd"
    elif number < 0:
        if number % 2 == 0:
            return "Negative Even"
        else:
            return "Negative Odd"
    else:
        return "Zero"

print(check_number(10))
print(check_number(-8))
print(check_number(0))
print(check_number(7))
print(check_number(-7))"""

                                #Final Test — Question 3

"""students = {
    "Hardik": 85,
    "Bhoomi": 92,
    "Neha": 35,
    "Rahul": 67
}

pass_marks = 40

def show_result(students):

    for name, marks, in students.items():
        if marks >= pass_marks:
            print(name, ":", marks, "Pass")
        else:
            print(name, ":", marks, "Fail")
show_result(students)
"""

                            #Final Test — Question 4
"""try:
    def divide_numbers(num1, num2):
        return num1 / num2
    print(divide_numbers(10, 2))
    print(divide_numbers(10, 0))
except ValueError:
    print("Invalid Input")
except ZeroDivisionError:
    print("Cannot Divide By Zero")
"""

                                #Question 5 — Final Mini Challenge
# Total Students :
# Average Marks :
# Highest Marks :
# Lowest Marks :
# Passed :
# Failed :
"""
students = {
    "Hardik": 85,
    "Bhoomi": 92,
    "Neha": 35,
    "Rahul": 67
}

pass_marks = 40
def analyze_students(students):
    highest = float("-inf")
    lowest = float("inf")
    passed = 0
    failed = 0
    total = 0
    for name, marks, in students.items():
        if marks > highest:
            highest = marks
        if marks < lowest:
            lowest = marks

        if marks >= pass_marks:
            passed += 1
        else:
            failed += 1
        total = total + marks
    avg = total / len(students)
    return highest, lowest, passed, failed, total,avg
result = analyze_students(students)
print(result)

"""

#Task 1

"""year = int(input("Enter Your Birth Year :"))
answer = 2026 - year
print("You are", answer, "Years Old!!")"""

#task 2
"""
score = int(input("Enter Your Score from 1 to 100 :"))

if score >= 90:
    print("Awesome!! Grade A")
elif 50 <= score <= 89:
    print("Good Job!! You Passed")
else:
    print("Needs Improvement!!! Failed")
"""

#task 3
"""
foods = ["pizza", "burger", "tacos"]

for food in foods:
    print("Fav Food", food.upper())
"""

# task 4
"""
numbers = [5, 10, 5, 20, 10]

unique = set(numbers)
count = len(unique)
print("Count :", count)

num = [5, 10, 5, 20, 10]
my_data = set(num)

data = {
    "name": "Hardik",
    "unique_numbers": my_data
}
print(my_data)
"""

#task 5
"""
def safe_divide():
    a = int(input("Enter Number 1 :"))
    b = int(input("Enter Number 2 :"))   
    return a / b

while True:
    try:
        result = safe_divide()
        print("Result :", result)
        break
    
    except ValueError:
        print("Invalid Input")
    except ZeroDivisionError:
        print("Cannot Divide By Zero")"""

#1
"""
name = input("Enter Your Name :")
budget = int(input("Enter Your Budget :"))

massage = f"Welcome, {name}, {budget}"
print(massage)
"""
#2

"""
app = ("Finance Tracker v1.0", "Hardik")

categories = {
    "Food": 500,
    "Transport": 150,
    "Bills": 1550,
    "Entertainment": 4000
}
expense_list = []

def calculate_avg(total_spent, count):
    try:
        return total_spent / count
    except ZeroDivisionError:
        return 0.0
    
while True:
    print("\n----------------------------------------")
    print("1: Add New Expense")
    print("2: View All Expenses & Remaining Budget")
    print("3: Calculate Average Expense")
    print("4: Exit")
    print("----------------------------------------")

    choice = input("Enter Your Choice: ").strip()

    if choice == "1":
        category_input = input("Enter category: ").strip().title()
        
        if category_input in categories:
            try:
                amount_input = float(input(f"Enter Amount Spent for {category_input}: "))
                
                new_expense = {
                    "amount": amount_input,
                    "category": category_input
                }
                expense_list.append(new_expense)

                categories[category_input] -= amount_input
                print(f"Successfully added ${amount_input} to {category_input}!")
            except ValueError:
                print("Enter Valid Amount")
        else:
            print("Invalid Category !! Pick a valid one.")

    elif choice == "2":
        print("\n--- All Expenses Logged ---")
        if not expense_list:
            print("No Expenses Added Yet")
        else:
            for item in expense_list:
                print(f"- ${item['amount']} spent on {item['category']}")

        print("\n--- Remaining Budgets ---")
        for category, budget in categories.items():
            print(f"- {category}: ${budget:.2f} remaining")

    elif choice == "3":
        total_spent = sum(item["amount"] for item in expense_list)
        total_count = len(expense_list)

        avg = calculate_avg(total_spent, total_count)
        print(f"\nTotal Spent: ${total_spent:.2f} across {total_count} transaction(s).")
        print(f"Average Expense: ${avg:.2f}")
    
    elif choice == "4":
        print(f"Thank You For Using {app[0]} by {app[1]}!")
        break

    else:
        print("Invalid Option!! Choose between 1 to 4")
"""

"""
#Exercise 1 — Personal Information

name = "Hardik"
age = 23
height = 163.5
student_status = True
fav_language = "Python"

print(name)
print(age)
print(height)
print(student_status)
print(fav_language)

#Exercise 2 — Data Type Checker

name = "Hardik"
age = 24
height = 163.5
student = True

print(type(name))
print(type(age))
print(type(height))
print(type(student))

#Exercise 3 — Swap Two Variables

a = 10
b = 20

a,b = b,a

print(a)
print(b)

#Exercise 4 — Basic Calculator
# Addition
# Subtraction
# Multiplication
# Division
# Modulus

num_1 = int(input("Enter Number 1 :"))
num_2 = int(input("Enter Number 2 :"))

print("Add :", num_1 + num_2)
print("Sub :", num_1 - num_2)
print("Multi :", num_1 * num_2)
print("Divi :", num_1 / num_2)
print("Mod :", num_1 % num_2)

#Exercise 5 — Rectangle Calculator

length = int(input("Enter Length :"))
width = int(input("Enter Width :"))

Area = length * width
print("Area :", Area)

perimeter = 2 * (length + width)
print("Perimeter :", perimeter)


#Exercise 6 — Temperature Converter

calcius = int(input("Enter Calcius :"))

fahrenheit = (calcius * 9/5) + 32
print("Fahrenheit :", fahrenheit)


#Exercise 7 — Simple Interest

principal = int(input("Enter Amount :"))
rate =  float(input("Enter Rate :"))
time = int(input("Enter Time :"))

simple_intrest = (principal * rate * time) / 100
print("SI :", simple_intrest)


#Exercise 8 — Positive / Negative / Zero

num = int(input("Enter Number :"))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


#Exercise 9 — Even / Odd

num = int(input("Enter Number :"))

if num % 2 == 0:
    print("Number Is Even")
else:
    print("Number Is Odd")


#Exercise 10 — Largest of Two

num_1 = int(input("Enter Number 1 :"))
num_2 = int(input("Enter Number 2 :"))

if num_1 > num_2:
    print("Largest Number Is :", num_1)
else:
    print("Largest Number Is :", num_2)

#Exercise 11 — Largest of Three

num_1 = int(input("Enter Number 1 :"))
num_2 = int(input("Enter Number 2 :"))
num_3 = int(input("Enter Number 3 :"))

if (num_1 >=num_2) and (num_1 >= num_3):
    print("Largest Number :", num_1)
elif (num_2 >=num_1) and (num_2 >= num_3):
    print("Largest Number :", num_2)
else:
    print("Largest Number :", num_3)


#Exercise 12 — Grade Calculator

marks = int(input("Enter Marks : "))

if 90 <= marks <= 100:
    print("Grade A")
elif 80 <= marks <= 89:
    print("Grade B")
elif 70 <= marks <= 79:
    print("Grade C")
elif 60 <= marks <= 69:
    print("Grade D")
elif 50 <= marks <= 59:
    print("Grade E")
elif 40 <= marks <= 49:
    print("Grade F")
else:
    print("Fail")


#Exercise 13 — Positive/Negative + Even/Odd

def check_number(number):
    if number > 0:
        print("Positive")
        if number % 2 ==0:
            print("Positive Even")
        else:
            print("Positive odd")
    elif number < 0:
        print("Negative")
        if number % 2 ==0:
            print("Negative Even")
        else:
            print("Negative Odd")
    else:
        print("Zero")
check_number(8)
check_number(7)
check_number(-8)
check_number(-7)
check_number(0)



#Exercise 14 — Numbers 1–20

for i in range(1,21):
    print(i)

#Exercise 15 — Even Numbers

for i in range(0,51,2):
    print(i)

#Exercise 16 — Odd Numbers

for i in range(1,51,2):
    print(i)

#Exercise 17 — Multiplication Table

num = int(input("Enter Number :"))

for i in range(1,11):
    print(num, "X", i, "=", num * i)


#Exercise 18 — Sum 1–100
total = 0
for i in range(1,101):
    total += i
print("Sum :", total)

#Exercise 19 — Count Numbers

even = 0
odd = 0

for i in range(1, 51):
    if i % 2 ==0:
        even += 1
    else:
        odd += 1
print("Even Count :", even)
print("Odd Count :", odd)



#Exercise 20 — Countdown WHILE LOOP

count = 10
while count >= 1:
    print(count)
    count -= 1

#Exercise 21 — Number Guessing
import random

random_number = random.randint(1,50)
max_attempts = 5
attempts = 0

while attempts < max_attempts:

    guess_number = int(input("Enter Guess Number :"))
    attempts += 1

    if guess_number == random_number:
        print("Yeahh You Win!!")
        break
    elif guess_number > random_number:
        print("Too High")  
    else:
        print("Too low")
else:
    print("Game Over...!!!")

print("attempts :", attempts)

#Exercise 22 — Limited Attempts


#Exercise 23 — Square Function

def square(number):
    return number * number
print(square(5))
print(square(8))

#Exercise 24 — Even/Odd Function

def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(check_even_odd(4))
print(check_even_odd(5))

#Exercise 25 — Largest Function

def find_largest(a, b, c):
    if (a >= b,) and (a >= c):
        return "largest", a
    elif (b >= a) and (b >= c):
        return "largest", b 
    else:
        return "largest", c
print(find_largest(40,50,60))
print(find_largest(30,40,50))
print(find_largest(20,30,40))

#Exercise 26 — Calculator Function

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
        return "Invalid Input"
result = calculator(10,"*",50)
print("Result :", result)


#Exercise 27 — List Analyzer

numbers = [10, 25, 7, 40, 15]
print(max(numbers))
print(min(numbers))
total = sum(numbers)
print(total)
avg = total / len(numbers)
print(avg)

#Exercise 28 — Even/Odd Count

numbers = [10, 25, 7, 40, 15, 8, 21]

even = 0
odd = 0
for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even Count :", even)
print("Odd Count :", odd)



#Exercise 29 — Five Number Analyzer

num1 = int(input("Enter Number 1:"))
num2 = int(input("Enter Number 2:"))
num3 = int(input("Enter Number 3:"))
num4 = int(input("Enter Number 4:"))
num5 = int(input("Enter Number 5:"))

nums = [num1,num2,num3,num4,num5]
total = 0
Average = 0
Largest = float("-inf")
Smallest = float("inf")
Even_Count = 0
Odd_Count = 0
for num in nums:
    if num % 2 ==0:
        Even_Count += 1
    else:
        Odd_Count += 1
    
    if num > Largest:
        Largest = num
    if num < Smallest:
        Smallest = num
    
    total = total + num
    Average = total / len(nums)

print("Total :", total)
print("Average :", Average)
print("Even Count :", Even_Count)
print("Odd Count :", Odd_Count)
print("Largest :", Largest)
print("Smallest :", Smallest)



#Exercise 30 — Search a List

numbers = [10, 25, 7, 40, 15]

num = int(input("Enter Number :"))

if num in numbers:
    print("Number Found")
else:
    print("Number Not Found!")


#Exercise 31 — String Analyzer

sentence = input("Enter Sentence :")

print(len(sentence))

words= sentence.split()
words_count = len(words)
print(words_count)

print(sentence.upper())
print(sentence.lower())


#Exercise 32 — Vowel Counter

sentence = input("Enter Sentence :")
vowels = "aeiouAEIOU"
consonants ="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

vowels_count = 0
consonants_count = 0

for char in sentence:
    if char in vowels:
        vowels_count += 1
    elif char in consonants:
        consonants_count += 1

print("Vowels Count :",vowels_count)
print("Consonants Count :", consonants_count)



#Exercise 33 — Space Counter

sentence = input("Enter Sentence :")

space_count = sentence.count(" ")
print("Space Count :", space_count)



#Exercise 34 — First & Last Character

name = "Hardik"

print(name[0])
print(name[-1])

#Exercise 35 — Reverse String

name = "Hardik"

reverse_text = name[::-1]
print(reverse_text)


#Exercise 36 — Tuple Basics

colors = ("Red", "Blue", "Green", "Yellow")

print(colors[0])
print(colors[-1])
print(len(colors))

#Exercise 37 — Tuple Search

numbers = (10, 20, 30, 40, 50)

num = int(input("Enter Number :"))

if num in numbers:
    print("Exist")
else:
    print("Not Exist")



#Exercise 38 — Remove Duplicates

numbers = [10, 20, 10, 30, 20, 40, 30]

unique_number = set(numbers)
print(unique_number)

unique_number_count = len(unique_number)
print(unique_number_count)


#Exercise 39 — Set Operations
numbers = [10, 20, 10, 30, 20, 40, 30, 50]

number_set = set(numbers)

print("Unique Numbers :", number_set)
print("Number of Unique Values :", len(number_set))

extra_numbers = {30, 40, 60, 70}

print("Union :", number_set.union(extra_numbers))
print("Intersection :", number_set.intersection(extra_numbers))

#Exercise 40 — Student Dictionary

student = {
    "name": "Hardik",
    "age": 24,
    "marks": 85
}

for key, value, in student.items():
    print(key, ":", value)



#Exercise 41 — Search Student
#Exercise 42 — Pass/Fail Results
def search_student(students, name):

    if name in students:
        return students[name]
    else:
        return "Student not found"

students = {
    "Hardik": 85,
    "Bhoomi": 92,
    "Neha": 78,
    "Rahul": 67
}
pass_marks = 40
for name, marks in students.items():
    if marks >= pass_marks:
        print(name, ":", marks,":", "Pass")
    else:
        print(name, ":", marks,":", "Fail")

print(search_student(students, "Bhoomi"))
print(search_student(students, "Anjali"))



#Exercise 43 — Student Analyzer

def student_analyzer(students):
    return students

students = {
    "Hardik": 85,
    "Bhoomi": 92,
    "Neha": 34,
    "Rahul": 20
}
print(len(students))
total = 0
average = 0
highest = float("-inf")
lowest = float("inf")
passed = 0
failed = 0
pass_marks = 40
for name, marks in students.items():
    if marks >= pass_marks:
        passed+= 1
    else:
        failed += 1
    
    if marks > highest:
        highest = marks
    if marks < lowest:
        lowest = marks

    total = total + marks
    average = total / len(students)
print("Total :", total)
print("Average :", average)
print("Highest :", highest)
print("Lowest :", lowest)
print("Passed Students :", passed)
print("Failed Students :", failed)



#Exercise 44 — Safe Division
try:
    num_1 = int(input("Enter Number 1 :"))
    num_2 = int(input("Enter Number 2 :"))

    result = num_1 / num_2
    print("Result :", result)

except ValueError:
    print("Invalid Input")
except ZeroDivisionError:
    print("Cannot Divide by zero")



#Exercise 45 — Safe Integer Input

try:
    num = int(input("Enter Number :"))
    print("Number Is:", num)
except ValueError:
    print("Invalid Input")



#Exercise 46 — Safe Calculator

try:
    num_1 = int(input("Enter Number 1 :"))
    operators = input("Enter Operators (+,-,*,/ ) :")
    num_2 = int(input("Enter Number 2 :"))

    if operators == "+":
        result = num_1 + num_2
    elif operators == "-":
        result = num_1 - num_2
    elif operators == "*":
        result = num_1 * num_2
    elif operators == "/":
        result = num_1 / num_2
    else:
        print("Invalid Operator")
        result = None
    if result is not None:
        print("Result :", result)
except ValueError:
    print("Invalid Input")
except ZeroDivisionError:
    print("Cannot Divide By Zero")


"""
#Exercise 47 — Number Analyzer Function

def analyze_number(number):

    if number > 0:
        sign = "Positive"

        if number % 2 == 0:
            number_type = "Even"
        else:
            number_type = "Odd"

    elif number < 0:
        sign = "Negative"

        if number % 2 == 0:
            number_type = "Even"
        else:
            number_type = "Odd"

    else:
        sign = "Zero"
        number_type = "Zero"

    return sign, number_type, number


print(analyze_number(10))
print(analyze_number(-7))
print(analyze_number(0))


#Exercise 48 — List Statistics Function

def analyze_list(numbers):

    minimum = float("inf")
    maximum = float("-inf")
    total = 0
    even = 0
    odd = 0
    for num in numbers:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num
            
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
            
        total += num
    average = total / len(numbers)

    return {
        "minimum": minimum,
        "maximum": maximum,
        "total": total,
        "average": average,
        "even": even,
        "odd": odd
    }
        
numbers = [43,53,66,88,75,90]
result = analyze_list(numbers)

print("Minimum :", result["minimum"])
print("Maximum :",result["maximum"])
print("Total :", result["total"])
print("Average :", result["average"])
print("Even Count :", result["even"])
print("Odd Count :", result["odd"])



#Exercise 49 — Student Search System

students = {
    "Hardik": 85,
    "Bhoomi": 92,
    "Neha": 34,
    "Rahul": 20
}

while True:
    print("1. Search Student")
    print("2.Show all Students")
    print("3.Exit")

    choice = input("Enter Your Choice :")

    if choice == "1":
        search = input("Search Student Name :")

        if search in students:
            print(search, ":", students[search])
        else:
            print("Student Not Found!!!")
    elif choice == "2":
        for name, marks in students.items():
            print(name, ":", marks)

    elif choice == "3":
        print("Exiting")
        break
    else:
        print("Invalid Choice")



#Exercise 50 — Mini ATM  

try:
    account = {
        "name": "Hardik",
        "Pin": 1111,
        "balance": 550000
    }
    print("\nWelcome to the ATM!!")
    print("Please Enter Your PIN..")

    max_attempts = 3
    attempts = 0
    running = False
    while attempts < max_attempts:
        user_pin = int(input("Enter Pin :"))

        if account["Pin"] == user_pin:
            print("Welcome!!", account["name"])
            running = True
            break
        else:
            attempts += 1
            remaining = max_attempts - attempts
            if remaining == 0:
                print("Access Denied")
            else:
                print("Incorrect Pin")

    while running:
        print("1.Check Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")

        choice = input("Enter Your Choice :")

        if choice == "1":
            for balance in account.values():
                print("Current Balance :",account["balance"])
            
        elif choice == "2":
            amount = int(input("Enter Deposit Amount :"))
            account["balance"] += amount
            print("Deposit Amount :", amount, "New Balance :", account["balance"])
        
        elif choice == "3":
            with_amount = int(input("Enter Withdraw Amount :"))

            if with_amount <= account["balance"]:
                account["balance"] -= with_amount
                print("Withdraw Amount :", with_amount, "Current Balance :", account["balance"])
            else:
                print("Insufficient balance")

        if choice == "4":
            print("Thank You For Using The ATM....!!!")
            running = False
except ValueError:
    print("Invalid Numeric Input")



#exercise 51- Student Management Console   

#1. Show Students
# 2. Add Student
# 3. Search Student
# 4. Show Highest
# 5. Show Lowest
# 6. Show Average
# 7. Show Pass/Fail Count
# 8. Exit

students = {
    "Hardik": 85,
    "Bhoomi": 92,
    "Neha": 34,
    "Rahul": 20,
    "Zeel": 39,
    "Priya": 60 
}
pass_marks = 40
def show_students():
    if not students:
        print("Studens Not Found")
        return
    print("\n Students :")
    for name, marks in students.items():
        print(name, ":", marks)
    
def add_students():
    name = input("Enter Name :")

    if not name:
        print("Name Cannot BE Empty..")
        return
    
    marks = int(input("Enter Student Marks :"))

    if marks < 0 or marks > 100:
        print("Marks Must Be Between 0 to 100...!!")
        return

    students[name] = marks
    print("Saved Info :", name)

def search_student():
    name = input("Search Student Name :")

    if name in students:
        print(name, ":", students[name])
    else:
        print("Student Not Found!!!")

def show_highest():
    if not students:
        print("Student Not Found!!!")
        return

    max_marks = max(students.values())

    print("Highest Scorer :")
    for name, marks in students.items():
        if marks == max_marks:
            print(name, ":",marks)

def show_lowest():
    if not students:
        print("Student Not Found!!!")
        return
    
    lowest_marks = min(students.values())

    print("Lowest Scorer :")
    for name, marks in students.items():
        if marks == lowest_marks:
            print(name, ":",marks)

def show_average():
    if not students:
        print("Student Not Found!!!")
        return
    
    total_marks = sum(students.values())
    avg = total_marks / len(students)

    print("Average Marks :", avg)

def show_pass_fail():
    if not students:
        print("Student Not Found!!!")
        return
    
    passed = sum(1 for marks in students.values() if marks >= pass_marks)
    failed = len(students) - passed

    print("Passed Students :", passed)
    print("Failed Students :", failed)

while True:
    print("1. Show Students")
    print("2. Add Student")
    print("3. Search Student")
    print("4. Show Highest")
    print("5. Show Lowest")
    print("6. Show Average")
    print("7. Show Pass/Fail Count")
    print("8. Exit")

    choice = input("Enter Your Choice :")

    if choice == "1":
        show_students()
    elif choice == "2":
        add_students()
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
        print("Exiting....")
        break
    
    else:
        print("Please enter a number from 1 to 8.")

