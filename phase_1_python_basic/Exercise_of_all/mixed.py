



                            #1======================
                                # Highest mark
                                # Lowest mark
                                # Total
                                # Average
                            #1======================

# marks = [75, 80, 95, 60, 85]
# print(max(marks))
# print(min(marks))
# print(sum(marks))

# average = sum(marks) / len(marks)

# print("Average = ", average)


#                             #2=====================================
#                                     # First country
#                                     # Last country
#                                     # Total countries
#                                     # Slice only the middle two countries
#                             #2=====================================

# countries = ("India", "Germany", "Japan", "Canada")

# print(countries[0])
# print(countries[-1])
# print(len(countries))
# print(countries[1:3])


#                             #3=====================================
#                                     # Total unique numbers
#                                     # Add 50
#                                     # Remove 20 using discard()
#                                     # Print final set
#                             #3=====================================
                        
# numbers = {10,20,30,20,40,10}

# print(numbers)
# numbers.add(50)
# numbers.discard(20)
# print(numbers)

#                             #4=====================================
#                                         # Even numbers
#                                         # Odd numbers
#                             #4=====================================

# numbers = [10,15,20,25,30,35]


# even_count = 0
# odd_count = 0
# for num in numbers:
#     if num % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1
# print("Even Count =", even_count)
# print("Odd_Count = ",odd_count)


#                             #5=====================================
#                                        #FOUND NOT FOUND
#                             #5=====================================

# fruits = ["Apple","Banana","Mango","Orange"]

# if "Mango" in fruits:
#     print("Found")
# else:
#     print("Not Found")

#                             #6=====================================
#                                     # How many Blue
#                                     # Index of Green                                      
#                             #6=====================================

# colors = ("Red","Blue","Green","Blue")
# print(colors.count("Blue"))
# print(colors.index("Green"))


#                             #7=====================================
                                     
#                             #7=====================================

# students = {
#     "Hardik",
#     "Rahul",
#     "Priya"
# }

# for student in students:
#     print("Welcome ", student)

#                             #8=====================================
                                       
#                             #8=====================================

# numbers = [10,20,30,40,50]

# for num in numbers:
#     if num % 2 == 0:
#         print(num, "Is Even")

#                             #9=====================================
#                                        #FUNCTION
#                             #9=====================================
# def greet(name):
#     print("Welcome ", name)

# greet("Hardik")


#                                             #10
# def findLargest(numbers):
#     return max(numbers)

# result = findLargest([50,80,20,100])
# print(result)


#                             #9=====================================
#                             # ALL IN ONE
#                                         # Largest Number
#                                         # Smallest Number
#                                         # Total
#                                         # Average
#                                         # Even Count
#                                         # Odd Count
#                             #9=====================================

# numbers = [10,20,30,40,50]
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))

# Avg = sum(numbers) / len(numbers)
# print("Average =", Avg)

# even_count = 0
# odd_count = 0
# for num in numbers:
#     if num % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1
# print("Even Count =", even_count)
# print("Odd Count =", odd_count)



#1
# Largest number
# Smallest number
# Total
# Averag

# numbers = [12, 25, 18, 40, 33]
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))

# average = sum(numbers) / len(numbers)
# print("Average = ", average)


# #2
# # First city
# # Last city
# # Total cities
# # Middle three cities

# cities = ("Ahmedabad", "Berlin", "Tokyo", "Paris", "London")
# print(cities[0])
# print(cities[-1])
# print(len(cities))
# print(cities[1:4])

# #3
# # Total unique numbers
# # Add 60
# # Remove 30
# # Print the final set

# numbers = {10, 20, 10, 30, 40, 20, 50}
# print(len(numbers))
# numbers.add(60)
# numbers.discard(30)
# print(numbers)


# #4
# # Even numbers
# # Odd numbers

# numbers = [5, 10, 15, 20, 25, 30]
# even = 0
# odd = 0
# for num in numbers:
#     if num % 2 == 0:
#         even += 1
#     else: 
#         odd += 1
# print("Even Num :", even)
# print("Odd Num :", odd)

# #5
# # How many students passed (>=40)
# # How many students failed (<40)

# marks = [35, 70, 90, 25, 80]

# pass_count = 0
# fail_count = 0
# for mark in marks:
#     if mark >=40:
#         pass_count += 1
#     else:
#         fail_count += 1
# print("Pass :", pass_count)
# print("Fail :", fail_count)

# #6
# #FOUND NOT FOUND

# names = ["Hardik", "Rahul", "Priya", "Aman"]

# if "Priya" in names:
#     print("Found")
# else:
#     print("Not Found")

# #7
# def square(num):
#     return num * num

# result = square(6)

# print("Ans =", result)

# #8
# def isEven(num):
    
#     if num % 2 ==0:
#         return True
#     else:
#         return False

# result = isEven(9)
# print(result)

# #9
# def findSmallest(numbers):
#     return findSmallest

# num = [10,9,11,15,19,25]
# print(min(num))

# #10
# numbers = [10, 15, 20, 25, 30]

# for num in numbers:

#     if num % 2 == 0:
#         print(num, "Is Even")
#     else:
#         print(num,"Is Odd")

# #11
# # How many times "Blue" appears
# # Index of "Green"
# # Last three colors using slicing

# colors = ("Red", "Blue", "Green", "Blue", "Yellow")

# print(colors.count("Blue"))
# print(colors.index("Green"))
# print(colors[2:])

# #12
# languages = {"Python", "Java"}

# languages.add("C++")
# languages.add("JavaScript")
# languages.remove("Java")
# print(languages)

# #13
# # Largest
# # Smallest
# # Total
# # Average
# # Even Count
# # Odd Count
# # Passed numbers (>=20)
# # Failed numbers (<20)

# numbers = [22, 15, 40, 13, 18, 50, 9]

# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))

# avg = sum(numbers) / len(numbers)
# print("Average =",avg)

# even = 0
# odd = 0
# for num in numbers:
#     if num % 2 == 0:
#         even += 1
#     else:
#         odd += 1
# print("Even Count =", even)
# print("Odd Count =", odd)

# pass_numbers = 0
# fail_numbers = 0

# for n in numbers:
#     if n >=20:
#         pass_numbers += 1
#     else:
#         fail_numbers += 1

# print("Pass Count = ",pass_numbers)
# print("Fail Count =", fail_numbers)


# #14  -- USING ONLY ONE LOOP 
# # Total
# # Average
# # Largest
# # Smallest

# numbers = [10, 20, 30, 40, 50]
# total = 0
# average = 0
# min_num = numbers[0]
# max_num = numbers[0]
# for num in numbers:
#     total =total + num
#     average = total / len(numbers)

#     if num < min_num:
#         min_num = num

#     if num > max_num:
#         max_num = num

# print(total)
# print(average)
# print(max_num)
# print(min_num)



# #1
# numbers = [12, 7, 18, 25, 30, 9]
# print(len(numbers))
# print(max(numbers))
# print(min(numbers))

# even = 0
# odd = 0
# for num in numbers:
#     if num % 2 == 0:
#         even += 1
#     else:
#         odd += 1
# print("Even Count =", even)
# print("Odd Count =", odd)

# #2
# movies = ("Interstellar", "Inception", "Avatar", "Titanic", "Joker")
# print(movies[0])
# print(movies[-1])
# print(len(movies))
# print(movies[1:4])
# print(movies.index("Avatar"))

# #3
# fruits = {"Apple", "Banana", "Apple", "Mango", "Orange", "Banana"}

# print(len(fruits))
# fruits.add("Grapes")
# fruits.discard("Mango")

# if "Apple" in fruits:
#     print("Exist")
# else:
#     print("Not Exist")

# for fruit in fruits: #you said loop through so thats why i print like this
#     print(fruit)

# #4
# def findAverage(numbers):
#     return average(numbers)

# num = [10, 20, 30, 40, 50]
# print(sum(num))

# average = sum(num) / len(num)

# print("Average =", average)

# #5
# marks = [85, 35, 70, 25, 95, 40]

# pass_count = 0
# fail_count = 0
# for mark in marks:
#     if mark >= 40:
#         pass_count += 1
#     else:
#         fail_count += 1
# print("Pass =", pass_count)
# print("Fail =", fail_count)

# print(max(marks))
# print(min(marks))
# avg = sum(marks) / len(marks)

# print("Average = ", avg)


# #6
# numbers = [25, 18, 42, 11, 60, 9]

# max_num = numbers[0]
# min_num = numbers[0]
# total = 0
# avg = 0
# for num in numbers:
#     total = total + num
#     if num < min_num:
#         min_num = num

#     if num > max_num:
#         max_num = num

#         avg = total / len(numbers)

# print(max_num)
# print(min_num)
# print(total)
# print("Average = ", avg)



                            #1 — List + Loop + Condition
# Print every even number
# Print every odd number
# Count even numbers
# Count odd numbers

numbers = [12, 7, 20, 15, 30, 9, 40]

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
print("Odd Count =",odd)

                                #2— List Statistics
# Find largest
# Find smallest
# Find total
# Find average
# Count marks >= 40
# Count marks < 40

# marks = [75, 82, 45, 91, 63, 38, 55]

# print(max(marks))
# print(min(marks))
# print(sum(marks))

# avg = sum(marks) / len(marks)
# print("Average =",avg)

# count_1=0
# count_2=0

# for mark in marks:
#     if mark >=40:
#         count_1 +=1
#     else:
#         count_2 +=1

# print("Marks >=40 ->",count_1)
# print("Marks <40 ->", count_2)


                            #3 — Tuple + String Methods
# Print first country
# Print last country
# Print middle three countries
# Find the index of "Japan"
# Check whether "Germany" exists

countries = ("India", "Germany", "Japan", "Canada", "France")
print(countries[0])
print(countries[-1])
print(countries[1:4])
print(countries.index("Japan"))

if "Germany" in countries:
    print("Exist")
else:
    print("Not Exist")
   
                            #4 — Set Practice
# Print total unique numbers
# Add 60
# Remove 30 using discard()
# Check whether 40 exists
# Print the final set
                          
# numbers = {10, 20, 10, 30, 40, 20, 50}

# print(len(numbers))
# numbers.add(60)
# numbers.discard(30)
# if 40 in numbers:
#     print("Exist")
# else:
#     print("Not Exist")

# print(numbers)

                                #5 — Dictionary Practice
# Print name
# Print dream
# Change country to "Canada"
# Add "language": "Python"
# Remove age
# Print every key and value

# student = {
#     "name": "Hardik",
#     "age": 24,
#     "country": "Germany",
#     "dream": "AI Engineer"
# }

# print(student["name"])
# print(student["dream"])

# student["country"] = "Canada"
# student.pop("age")

# for key, value, in student.items():
#     print(key, "=", value)

                                #6 — String + List
# Count "Python"
# Check if it starts with "Python"
# Check if it ends with "language"
# Split the sentence
# Print the first word
# Print the last word
                                
# sentence = "Python is my favorite language"
# print(sentence.count("python"))

# print(sentence.startswith("Python"))
# print(sentence.endswith("language"))
# print(sentence.split())
# print(sentence[0])
# print(sentence[-1])

        
                                    #7 — Function + Condition
# def is_pass(marks):
#         if marks >= 40:
#             return True
#         else:
#             return False

# print(is_pass(75))
# print(is_pass(35))


                                    #8 — Function + List
# def find_largest(numbers):

#     largest = numbers[0]

#     for num in numbers:
#             if num > largest:
#                 largest = num
#     return largest

# numbers = [25, 10, 90, 45, 60]
# Result = find_largest(numbers)
# print("The Largest Number Is =",Result)

                                    #9 — Mixed Challenge
# Find total
# Find average
# Find largest
# Find smallest
# Count even numbers
# Count odd numbers
# Count numbers >= 20
# Count numbers < 20  
                                  
# numbers = [15, 22, 8, 35, 40, 11, 50]
# even = 0
# odd = 0
# print(sum(numbers))

# average = sum(numbers) / len(numbers)
# print("Average =",average)

# print(min(numbers))
# print(max(numbers))

# for num in numbers:
#     if num % 2 == 0:
#         even += 1
#     else:
#         odd += 1
# print("Even Count =", even)
# print("Odd Count =", odd)
# num_1 = 0
# num_2 = 0
# for num in numbers:
#     if num >= 20:
#         num_1 += 1
#     else:
#         num_2 += 1
# print("Number >= 20 =>",num_1)
# print("Number < 20 =>",num_2)
                                        #10

# Print every student's name and mark.
# Count how many students passed (>= 40).
# Count how many failed (< 40).
# Find the highest mark.
# Find the lowest mark.
# Calculate the average mark.

# students = {
#     "Hardik": 85,
#     "Rahul": 35,
#     "Priya": 92,
#     "Aman": 45,
#     "Neha": 28
# }

# print(students)
# pass_count =0
# fail_count = 0
# for marks in students.values():
#     if marks >= 40:
#         pass_count += 1
#     else:
#         fail_count += 1
# print("Pass Count =", pass_count)
# print("Fail Count =", fail_count)

# max_marks = 0
# min_marks = 100
# for key, value in students.items():
#     if value > max_marks:
#         max_marks = value
#     if value < min_marks:
#         min_marks = value
# print(max_marks)
# print(min_marks)

# total_marks = 0

# for mark in students.values():
#     total_marks += mark

# average = total_marks / len(students)
# print("Average Marks =",average)




                                    #1 — Number Analyzer
# Largest number
# Smallest number
# Total
# Average
# Even count
# Odd count
# How many numbers are >= 20
# How many numbers are < 20

# numbers = [12, 45, 7, 30, 18, 55, 9]

# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))

# avg = sum(numbers) / len(numbers)
# print("Average :", avg)

# even = 0
# odd = 0
# num_1 = 0
# num_2 = 0
# for num in numbers:
#     if num % 2 == 0:
#         even += 1
#     else:
#         odd += 1
       
#     if num >= 20:  
#         num_1 += 1
#     else:
#         num_2 +=1

# print("Even Count :",even)
# print("Odd Count :",odd)
# print("Number >=20 :", num_1)
# print("Number < 20 :",num_2)



# #                                     #2 — Student Search
# students = {
#     "Hardik": 85,
#     "Rahul": 35,
#     "Priya": 92,
#     "Aman": 45
# }

# user = input("Enter Student Name :")

# if user in students:
#     print(user,":",students[user])
# else:
#     print("Student Not Found")


#                                     #3 — Word Analyzer
# # Total characters
# # Number of spaces
# # Number of words
# # Number of times "Python" appears
# # Sentence in uppercase
# # Sentence in lowercase

# sentence = input("Enter Your Sentence :")

# print(len(sentence))
# print(sentence.count(" "))
# print(sentence.count("Python"))
# print(sentence.upper())
# print(sentence.lower())
# print(sentence.startswith("I"))


#                                     # 4 — Safe Calculator Function

# # Invalid number
# # Division by zero
# # Invalid operator
# try:
#     number_1 = int(input("Enter Number 1:"))
#     operators = input("Enter Operators (+, -, *, /) :")
#     number_2 = int(input("Enter Number 2: "))

#     if operators == "+":
#         result = number_1 + number_2
#     elif operators == "-":
#         result = number_1 - number_2
#     elif operators == "*":
#         result = number_1 * number_2
#     elif operators == "/":
#         result = number_1 / number_2
#     else:
#         print("Invalid Operator")
#         result = None
#     if result is not None:
#         print("Answer :", result)
# except ValueError:
#     print("Invalid Input")
# except ZeroDivisionError:
#     print("Cannot Divide By Zero")



                                    #5 — Mini Student System


# try:
#     students = {
#         "Hardik" : 85,
#         "Rahul" : 35,
#         "Priya" : 92,
#         "Aman" : 45
#     }

#     max_marks = 0
#     min_marks = 100

#     for key,value, in students.items():
#         if value > max_marks:
#             max_marks = value
#         if value < min_marks: 
#             min_marks = value

#     print("Highest Marks :",max_marks)
#     print("Lowest Marks :",min_marks)

#     total = sum(students.values())
#     print("Total :",total)

#     avg = total / len(students)
#     print("Average :", avg)

#     pass_count = 0
#     fail_count = 0

#     for marks in students.values():
#         if marks >= 40:
#             pass_count += 1
#         else:
#             fail_count += 1
#     print("Pass Count :",pass_count)
#     print("Fail Count :", fail_count)

#     search = input("Enter Student Name :")

#     if search in students:
#         print(search, ":", students[search])
#     else:
#         print("Student Not Found !!")

#     for key,marks, in students.items():
#         if 90<= marks <=100:
#             print(key,":",marks,"Grade A")
#         elif 80 <= marks <= 89:
#             print(key,":",marks,"Grade B")
#         elif 70 <= marks <= 79:
#             print(key,":",marks,"Grade C")
#         elif 60 <= marks <= 69:
#             print(key,":",marks,"Grade D")
#         elif 40 <= marks <= 59:
#             print(key,":",marks,"Grade E")
#         else:
#             print(key,":",marks,"Fail")

# except ValueError:
#     print("Invalid Input") 
 

#===============================
#Largest
# Smallest
# Average
# Even count
# Odd count

# numbers = [15, 8, 42, 23, 10, 37]

# largest = 0
# smallest = 100
# even = 0
# odd = 0
# total = 0
# for num in numbers:
#     total = total + num
#     if num > largest:
#         largest = num
#     if num < smallest:
#         smallest = num
#     if num % 2 == 0:
#         even += 1
#     else:
#         odd += 1
    
# print("Largest Number :",largest)
# print("Smallest Number :",smallest)
# print("Even Count :",even)
# print("Odd Count :",odd)
# print("total :", total)

# avg = total / len(numbers)
# print("Average :", avg)



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

students = {
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
    print("Student Not Found")



