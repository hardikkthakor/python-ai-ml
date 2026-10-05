

#reduce()
#for use reduce() compolsory import reduce........


from functools import reduce
"""
# Q1 — Write code using reduce() + lambda
# Find the sum of all numbers.
numbers = [5, 10, 15, 20]

result = reduce(lambda a, b: a + b, numbers)
print(result)

# Q3 — Write code using a normal def function + reduce()
# Find the largest number.
numbers = [12, 45, 8, 90, 33]

def find_max(a,b):
    if a > b:
        return a
    else:
        return b

largest_num = reduce(find_max,numbers)
print(largest_num)


## Q1
# Find the total of all prices using reduce() + lambda.
prices = [499, 799, 250, 1200]

total_price = reduce(lambda a,b: a + b, prices)
print(total_price)


# Q2
# Find the product of all numbers using reduce() + lambda.
numbers = [1, 2, 3, 4, 5]
product_num = reduce(lambda a, b: a * b, numbers)
print(product_num)

# Q3
# Use a normal def function + reduce().
# Find the smallest number.
numbers = [25, 10, 45, 8, 32]

def find_smallest(a,b):
    if a < b:
        return a
    else:
        return b

smallest_num = reduce(find_smallest,numbers)
print(smallest_num)

# Q4
# First keep passing marks (mark >= 40) using filter().
# Then find their total using reduce().
marks = [35, 72, 20, 95, 40, 66]

passing_marks = list(filter(lambda mark: mark >= 40, marks))
total = reduce(lambda a,b: a + b, passing_marks)
print(passing_marks)
print(total)

# Q5
# Join all words into one sentence using reduce().
words = ["I", " ", "love", " ", "Python"]

join_words = reduce(lambda a, b: a + b, words)
print(join_words)
"""

#8. Real-World Mini Project — Seller Commission Calculator
"""
from functools import reduce

order_amounts = [350, 1200, 750, 2500, 999, 1800]

order = list(filter(lambda order: order >=1000, order_amounts))
commission = list(map(lambda order: order * 0.10, order))
total_commission = reduce(lambda a,b: a + b, commission)

print(f"Oder: {order}")
print(f"Commission: {commission}")
print(f"Total Commission: {total_commission}")
"""


# Q11
# Use reduce() + lambda to calculate the total expense.
expenses = [450, 1200, 300, 750, 500]
total_expense = reduce(lambda a,b: a + b, expenses)
print(total_expense)


# Q12
# Use a normal def function + reduce().
# Find the largest number.
numbers = [32, 75, 18, 96, 54]

def find_largest(a,b):
    if a > b:
        return a
    else:
        return b

largest_num = reduce(find_largest,numbers)
print(largest_num)


