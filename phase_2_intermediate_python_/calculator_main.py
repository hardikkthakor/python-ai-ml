


from calculator_package.basic import add, subtract
from calculator_package.advanced import square, cube

num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))

print("Addition:",add(num1, num2))
print("Subtraction:",subtract(num1, num2))

print("Square: ",square(num1))
print("Cube: ",cube(num2))
