


#1====================
# try:
#     num = int(input("Enter a Number :"))
#     print("You Entered :",num)
# except ValueError:
#     print("Invalid Number")



#2

# try:
#     num1 = int(input("Enter First Number :"))
#     num2 = int(input('Enter Second Number :'))
#     result = num1 / num2
#     print("Answer =", result)
# except ValueError:
#     print("Invalid Input")

# except ZeroDivisionError:
#     print("Cannot divided by Zero")



#3

try:
    num1 = int(input('Enter Number One :'))
    operator = input("Enter Operator (+, -, *, /)   :")
    num2 = int(input("Enter Number Two :"))

    if operator == "=":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    else:
        print("Invalid Operator")
        result= None
    if result is not None:
        print("Answer =", result)
except ValueError:
    print("Invalid Number")



