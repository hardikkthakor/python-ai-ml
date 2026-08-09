# count = 1

# while count <=25:
#     print(count)
#     count += 1


# count = 25

# while count >=1:
#     print(count)
#     count -= 1

# count = 2

# while count <=30:
#     print(count)

#     count += 2

# count = 1

# while count <=25:
#     print(count)
#     count += 2

# count = 100

# while count >=10:
#     print(count)
#     count -= 10



# number = int(input("Enter Your Number :"))
# count = 1

# while count <=15:
#     print(number, "X", count, "=", number * count)
#     count += 1


# number = int(input("Enter Your Number :"))
# count = 15

# while count >=1:
#     print(number, "X", count, "=", number * count)
#     count -= 1




# number = int(input("Enter Your Number :"))
# count = 2

# while count <=20:
#     print(number, "X", count, "=", number * count)
#     count += 2


# correct_password = "AI2026"

# password = ""

# while password != correct_password:
#     password = input("Enter Password :")
# print("Access Granted")


# correct_password = "Python@123"
# password = ""

# while password != correct_password:
#     password = input("Enter Password :")

#     if password != correct_password:
#         print("Wrong Password! Try Again.")
# print("Welcome!")


# count = 1

# while count <=20:
#     print(count)
#     if count ==14:
#         break
#     count +=1



# # p12 doubt explain this question in details
# count =1

# while count <= 20:
#     print(count)
#     if count % 5 ==0:
#         continue
#     count += 1


# # p13 also doubt explain this question in details
# count = 1

# while count <=20:
#     print(count)
#     if count %2 ==0:
#         continue
#     count += 1

# # p14 also doubt explain this question in details
# number = int(input("Enter Your Number :"))

# for i in range(1,11):
#     print(number , "X", i, "=", number * i)




#p1
# name = input("Enter Your Name :")
# marks = int(input("Enter Your Marks :"))

# if marks >=90:
#     print("Excellent Student")
# elif marks >=75:
#     print("Grade A")
# elif marks >=65:
#     print("Grade B")
# elif marks >= 35:
#     print("Grade C")
# else:
#     print("Faill")


#p2
# number = int(input("Enter Your Number :"))

# if number % 2 == 0:
#     print("Number Is Even")
# else:
#     print("Number is Odd")

# if number > 0:
#     print("Number Is Positive")
# else:
#     print("Number is Negative")



#p3
# number = int(input('Enter Your Number :'))
# count = 5
# while count <=15:
#     print(number, "X", count, "=", number * count)
#     count += 1


#p4

# total = 0
# count = 25

# while count <=75:
#     total = total + count
#     count += 1
# print(total)

#p5

# total = 0
# count = 20

# while count <=60:
#     total = total + count
#     count += 2
# print(total)


#p6

# correct_password = "Hardik123"
# password = ""

# while password != correct_password:
#     password = input("Enter Your Password :")

#     if password != correct_password:
#         print("Wrong Password Please try again")
    
# print("Welcome Buddy")


# p7 
# count = 1

# while count <=30:
#     if count % 5 == 0:
#         count +=1
#         continue
#     print(count)
#     count += 1


#p8
# number = int(input("Enter Number Between 1 to 20 :"))
# count = 1

# while count <=20:
#     if count == number:
#         break
#     print(count)
#     count += 1

#p9 i know the ans so i skip for now because im already late in sleeping
#p10 doubttt explain this also
# number = int(input("Enter Number :"))
# count = 2

# while count <= number:
#     if count % 2 == 0:
#         print(count)
#     count +=1


                        #=================================
                               #function day exersice 
                        #=================================


#1 STUDENT RESULT

# def result(name,marks):
#     if marks >=35:
#         return name +" : Pass"
#     else:
#         return name + " : Fail"
# print(result("Hardik",80))
# print(result("Priya",21))

# #2 REVESE TABLE 

# number = int(input("Enter Number :"))
# count = 10

# while count >=1:
#     print(number, "X", count, "=", number * count)
#     count -= 1

#3 sum of number using for loop

# total = 0
# for i in range(1,50):
#     total = total + i
# print(total)


#password using while

# correct_password = "Python2026"
# password = ""

# while password != correct_password:
#     password = input("Enter Password :")

#     if password != correct_password:
#         print("Wrong Password")
# print("Access Granted")

#largest number 

# def largest(a,b):
#     if a > b:
#         return a
#     else:
#         return b
# print(largest(9,4))

# def dream(country="Germany"):
#     print("My Dream Country is :", country)
# dream()
# dream("japan")
# dream("Canada")

# for i in range(1,21):
#     if i % 3 ==0:
#         continue
#     print(i)

# number = int(input("Enter Number bt 1 to 20 :"))
# count = 1

# while number <= 20:
#     if count == number:
#         break
#     print(count)
#     count += 1

# def square(numebr):
#     return numebr * numebr

# result = square(8)
# print(result)


# def calculator(a,b):
#     return a + b
# answer = calculator(15,25)
# print("Answer :", answer)


#1                  4/8/23

# marks = int(input("Enter Your Marks :"))

# if marks >= 75:
#     print("Distinction")
# elif  60<= marks <=74:
#     print("First Class")
# elif 35<= marks <=59:
#     print("Second Class")
# else:
#     print("Fail")


#2

# number = int(input("Enter Your Number :"))

# if number > 0:
#     print("Positive")
# elif number < 0:
#     print("Negative")
# else: 
#     print("Zero")


#3
# age = int(input("Enter Your Age :"))

# if age >=20:
#     print("Adult")
# elif 13<= age <=19:
#     print("Teenager")
# else:
#     print("Child")


#4
# num1 = int(input("Enter Number 1:"))
# num2 = int(input("Enter Number 2:"))

# if num1 > num2:
#     print(num1)
# else:
#     print(num2)

#5

# year = int(input("Enter Your Year :"))

# if year %2 == 0:
#     print("Even Year")
# else:
#     print("Odd Year")

#6

# for i in range(10,101,10):
#     print(i)


#7

# for i in range(51,100,2):
#     print(i)

#8

# number = int(input("Enter Number :"))

# for i in range(3,16):
#     print(number, "X", i, "=", number * i)

#9

# total = 0

# for i in range(50,101):
#     total = total + i
# print(total)


#10  

# total = 0

# for i in range(20,61,2):
#     total = total + i
# print(total)


#11             WHILE LOOP

# count = 30
# while count >=1:
#     print(count)
#     count -= 1

#12
# number= int(input("Enter Number :"))
# count = 15

# while count >=5:
#     print(number, "X", count, "=", number * count)
#     count -= 1

#13

# correct_password = "AIEngineer"
# password = ""

# while password != correct_password:
#     password = input("Enter Pass:")

#     if password != correct_password:
#         print("Wrong Pass")
# print("Welcome Buddy")

#14 

# count =1

# while count <=25:
#     if count == 18:
#         break
#     print(count)
#     count +=1

#15

# count = 1

# while count <=20:
#     if count % 4 ==0:
#         count +=1
#         continue

#     print(count)
#     count +=1

#16

# count = 50

# while count <=100:
#     if count ==75:
#         break
#     print(count)
#     count += 1


#17      FUNCTION

# def cube(number):
#     return number ** 3
# ans = cube(5)
# print("Answer :",ans)

#18

# def student(name,marks):
#     if marks >=35:
#         return name + " : Pass"
#     else:
#         return name + " : Fail"
# print(student("Hardik", 99))
# print(student("Priya", 21))


#19

# def greeting(name="ChatGPT"):
#     print("Hello", name)
# greeting()


#20

# def calculator(a,b):
#     return a + b, a - b, a * b
# result = calculator(10,5)
# print("Ans :", result)



#1

# marks = int(input("Enter Marks :"))

# if marks >= 90:
#     print("Exellent")
# elif 75 <= marks <=89:
#     print("Grade A")
# elif 50<= marks <=74:
#     print("Grade B")
# else:
#     print("Fail")
 

#2
# number = int(input("Enter Number :"))

# if number > 0:
#     print("Positive")
# elif number < 0:
#     print("Negative")
# else:
#     print("Zero")

#3
# for i in range(15,31):
#     print(i)

#4
# for i in range(1,26,2):
#     print(i)

#5
# num = int(input("Enter Number :"))
# count =12
# while count >=1:
#     print(num , "X", count, "=", num * count)
#     count -= 1

#6
# correct_Pass = "PythonAI2026"
# password = ""

# while password != correct_Pass:
#     password = input("Enter Pass :")

#     if password != correct_Pass:
#         print("Wrong Pass")
# print("Welcome Dude")

#7
# count = 1
# while count <=30:
#     if count == 18:
#         break
#     print(count)
#     count += 1

#8
# count = 1
# while count <= 20:
#     if count % 4 == 0:
#         count += 1
#         continue
#     print(count)
#     count += 1


#9
# def square(number):
#     return number * number
# result = square(4)
# print(result)

#10
# def eligible(age):
#     if age >=18:
#         return "Eligible"
#     else:
#         return "Not Eligible"
# ans = eligible(14)
# print(ans)

#11
# def dream(country="Germany"):
#     print("My Dream Country Is ", country)
# dream()

#12
# def calculator(a, b):
#     return a +b, a - b, a * b
# ans = calculator(10,5)
# print(ans)

#13
# fruits = ["Apple", "Banana", "Mango","Orange", "Grapes"]
# print(fruits[0])
# print(fruits[-1])

#14
# marks = [70, 80, 90]
# marks[1]= 85
# print(marks)

#15
# friends = ["Rahul", "Aman"]
# friends.append("Hardik")
# friends.append("Priya")
# print(friends)

#16
# numbers = [10, 30, 40]
# numbers.insert(1,20)
# print(numbers)

#17
# countries = ["India", "Germany", "Japan", "Canada"]
# countries.remove("Germany")
# print(countries)
# #18
# countries.pop(-1)
# print(countries)


#19
# num = [10,30,20,50,40]
# num.sort()
# print(num)

# num.sort(reverse=True)
# print(num)

#20
# languages = ["Python", "Java", "C++", "JavaScript"]
# languages.reverse()
# print(languages)

# print(len(languages))

# #21
# def student(name, marks):
#     if marks >35:
#         return name + " : Pass"
#     else:
#         return name + " : Fail"
# print(student("Hardik",99))
# print(student("Priya",21))

# students = ["Hardik", "Rahul", "Priya"]
# print(students)

# print(len(students))

# students.append("Aman")
# print(students)

# students.reverse()
# print(students)



                        #===========================
                            #NESTED LOOP EXERCISES
                        #===========================
#1
for i in range(1,6):
    for j in range(i):
        print("#", end=" ")
    print()

#2
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j,end=" ")
    print()

#3
letters = ["A", "B", "C", "D"]
 
for i in range(1, 5):
    for j in range(i):
        print(letters[j], end=" ")
    print()

#4
for i in range(1,6):
    for j in range(6 - i):
        print(i, end=" ")
    print()

5
for i in range(1,6):
    for j in range(5, i -1, -1):
        print(j, end="")
    print()

#6
for i in range(0,4):
    for j in range(i,-1,-1):
        print(j, end="")
    print()

#7
letters = ["A", "B", "C", "D", "E"]

for i in range(0,5):
    for j in range(i + 1):
        print(letters[i], end=" ")
    print()

#8
for i in range(5,0,-1):
    for j in range(1,i + 1):
        print(j, end="")
    print()

#9
for i in range(5,0,-1):
    for j in range(1, i + 1):
        print("*", end="")
    print()       #i know its wrong buddy

#10
for i in range(1,6):
    for j in range(i, 0, -1):
        print(j, end="")
    print()





                                #1. Even or Odd
# # Take a number.
# # Check whether it is even or odd.

# number = int(input("Enter Number :"))

# if number % 2 == 0:
#     print("Number Is Even")
# else:
#     print("Number is Odd")


#                             #2 Positive, Negative or Zero
# # Take a number.
# # Print whether it is positive, negative, or zero.

# num = int(input("Enter Number :"))

# if num > 0:
#     print("Number Is Positive")
# elif num < 0:
#     print("Number is Negative")
# else:
#     print("Number is Zero")


#                             #3 Largest of Three Numbers
# # Take 3 numbers.
# # Find the largest using conditions.

# num1 = int(input("Enter Number 1 :"))
# num2 = int(input("Enter Number 2 :"))
# num3 = int(input("Enter Number 3 :"))

# if num1 and num2 < num3:
#     print("Largest Number Is Number 3")
# elif num3 and num2 <  num1:
#     print("Largest is Number 1  ")
# else:
#     print("Largest Number Is Number 2:")


                                #4 Simple Calculator

# Take two numbers and an operator + - * /.
# Perform the operation.
# Handle invalid input with try/except.

# try:

#     num1 = int(input("Enter Number 1 :"))
#     operator = input("Enter Operator (+, -, *, /) : ")
#     num2 = int(input("Enter Number 2 :"))

#     if operator == "+":
#         result = num1 + num2
#     elif operator == "-":
#         result = num1 - num2
#     elif operator == "*":
#         result = num1 * num2
#     elif operator == "/":
#         result = num1 / num2
#     else:
#         print("Invalid Operators")
#         result = None
#     if result is not None:
#         print("Answer :", result)
# except ValueError:
#     print("Invalid Number")


                            #5 Temperature Converter

# Create a program that converts:

# Celsius → Fahrenheit
# Fahrenheit → Celsius