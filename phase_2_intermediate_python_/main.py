




import my_module

print(my_module.greet("Hardik"))
print(my_module.square(5)) 

from my_module import greet,square

print(greet("Hardik"))
print(square(5))


from my_module import greet, square

print(greet("Hardik"))
print(square(12))


# #Exercise 4 — Custom Utility Module-------(this is part of module_exercises.py)
# from my_module import cube,is_even

# number = int(input("Enter Number :"))

# print(cube(number))
# print(is_even(number))