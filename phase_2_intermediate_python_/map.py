
"""
# Q1 — Write code using map() + lambda
# Double every item in:
numbers = [5, 10, 15, 20]

result = list(map(lambda num: num * 2, numbers))
print(result)

# Q3 — Write code using a normal def function + map()
# Convert every number in this list to its cube:
def cube(n):
    return n ** 3

numbers = [1, 2, 3, 4]

cubed_num = list(map(cube, numbers))
print(cubed_num)
"""
"""# Q1
# Add 5 to every number.
numbers = [10, 20, 30, 40]

result = list(map(lambda num: num + 5, numbers))
print(result)

# Q2
# Convert each name to uppercase.
names = ["hardik", "python", "software engineer"]

uppercase_names = list(map(lambda name: name.upper(), names))
print(uppercase_names)

# Q3
# Convert Celsius temperatures to Fahrenheit.
# Formula: (celsius * 9 / 5) + 32
celsius = [0, 10, 25, 100]

fahrenheit = list(map(lambda cels: (cels * 9/5) + 32,celsius))
print(fahrenheit)

# Q4
# Multiply matching items from both lists.
prices = [100, 250, 50]
quantities = [2, 3, 5]


multiply = list(map(lambda a,b: a * b, prices,quantities))
print(multiply)

# Q5
# Convert every string into an integer.
values = ["10", "25", "100", "7"]
# Hint: int is already a built-in function, so you can pass it to map().
result = list(map(int,values))
print(result)
"""



#8. Real-World Mini Project — Online Store Calculator

"""products = ["Keyboard", "Mouse", "USB Cable", "Headphones"]

prices = [499, 799, 250, 1200]

quantities = [2, 1, 4, 1]

item_total = list(map(lambda a,b: a * b, prices, quantities))

discount = list(map(lambda total: total * 0.9 if total >= 1000 else total ,item_total,))
full_total = sum(item_total)
full_total_discount = sum(discount)
print(f"Item Total Before Discount:{item_total}")
print(f"Item Total After Discount:{discount}")
print(f"Full Total Before Discount: {full_total}")
print(f"Full Total After Discount: {full_total_discount}")
"""

# Q10
# Use map() + lambda to convert:
numbers = [1, 2, 3, 4]
# into cubes

result = list(map(lambda num: num ** 3, numbers))
print(result)

# Q11
# Use map() with a normal def function.
# Add 18% GST to each price:
prices = [100, 500, 1000]

def add_gst(price):
    return price * 1.18

result = list(map(add_gst, prices))
print(result)

# Q12
# Use map() with two lists to calculate total marks.
theory_marks = [25, 30, 28]
practical_marks = [70, 65, 72]

total = list(map(lambda a,b: a + b,theory_marks,practical_marks))
print(total)
