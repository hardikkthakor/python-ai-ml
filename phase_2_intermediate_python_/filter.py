


"""
# Q1 — Write code
# Keep only numbers divisible by 3.
numbers = [3, 5, 6, 10, 12, 14, 18]

result = list(filter(lambda num: num % 3 == 0, numbers))
print(result)

# Q2 — Write code using a normal def function + filter()
# Keep only passing marks (marks >= 40).
marks = [35, 40, 72, 20, 95, 39]

def pass_marks(mark):
    return mark >= 40

result = list(filter(pass_marks,marks))
print(result)

# Q4 — Use filter() and map() together
# Keep only positive numbers, then square them.
numbers = [-2, 3, -5, 4, 0, 6]

pos_square = list(map(lambda num: num ** 2, filter(lambda num: num > 0, numbers)))
print(pos_square)

"""
"""# Q1
# Keep only multiples of 5.
numbers = [5, 12, 15, 18, 20, 23, 25]

result = list(filter(lambda num: num % 5 == 0, numbers))
print(result)

# Q2
# Use a normal def function + filter().
# Keep only distinction marks (marks >= 75).
marks = [65, 75, 82, 49, 91, 70]
def mark(m):
    return m >= 75
result = list(filter(mark, marks))
print(result)

# Q3
# Keep only names with more than 5 letters.
names = ["AI", "Python", "Java", "Hardik", "Developer"]

updated_name = list(filter(lambda name: len(name) > 5, names))
print(updated_name)

# Q4
# First keep even numbers, then convert them into cubes.
numbers = [1, 2, 3, 4, 5, 6]
even_num = list(filter(lambda num: num % 2 == 0, numbers))
cube = list(map(lambda num: num ** 3, even_num))
print(even_num)
print(cube)

# Q5
# Keep only adults (age >= 18).
ages = [12, 18, 21, 16, 30, 17]

adult = list(filter(lambda age: age >= 18, ages))
print(adult)


#8. Real-World Mini Project — Student Result Analyzer

marks = [35, 72, 89, 20, 95, 40, 66, 38, 78, 55]

passed_marks = list(filter(lambda mark: mark >= 40, marks))
failed_marks = list(filter(lambda mark: mark < 40, marks))
distinction_marks = list(filter(lambda mark: mark >= 75, marks))

print(f"Passed Students: {passed_marks}")
print(f"Failed Students: {failed_marks}")
print(f"Distinction Students: {distinction_marks}")

print("Passed Count:", len(passed_marks))
print("Failed Count:", len(failed_marks))
print("Distinction Count:", len(distinction_marks))
"""

# Q10
# Use filter() + lambda to keep only odd numbers.
numbers = [10, 11, 12, 13, 14, 15]

result = list(filter(lambda num: num % 2 != 0, numbers))
print(result)

# Q11
# Use a normal def function + filter().
# Keep products costing more than 500.
def product(price):
    return price > 500
prices = [250, 499, 500, 750, 1200]

updated_price = list(filter(product, prices))
print(updated_price)
# Q12
# First keep positive numbers, then double them using map().
numbers = [-5, 3, 0, 8, -2, 10]

positive_num = list(filter(lambda num: num > 0, numbers))
double_num = list(map(lambda num: num * 2, positive_num))

print(positive_num)
print(double_num)

