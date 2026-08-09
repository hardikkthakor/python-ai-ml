                        #=======================================
                                #PROJECT 1 CALCULATOR
                        #=======================================


try:
    number1 = int(input("Enter First Number :"))
    operator = input("Enter Operator(+, -, *, /) :")
    number2 = int(input("Enter Second Number ")) 

    if operator == "+":
        result = number1 + number2
    elif operator == "-":
        result = number1 - number2
    elif operator == "*":
        result = number1 * number2
    elif operator == "/":
        result = number1 / number2
    else:
        print("Invalid Operator")
        result = None
    if result is not None:
        print("Answer = ", result)
except ValueError:
    print("Invalid Number")
except ZeroDivisionError:
    print("Cannot Divided By Zero")