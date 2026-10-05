


#---------------------------
    #Generator
#---------------------------


# Q1 — Write a generator
# Yield numbers from 1 to n.
# Example: list(numbers_up_to(4)) → [1, 2, 3, 4]

def numbers_up(n):
    while n <= 4:
        yield n
        n += 1
    
print(list(numbers_up(1)))


# Q2 — Write a generator
# Yield only even numbers from a provided list.
# Example: list(even_numbers([1, 2, 3, 4, 5, 6]))
# → [2, 4, 6]

def even_num(numbers):
    for n in numbers:
        if n % 2 == 0:
            yield n
        
print(list(even_num([1,2,3,4,5,6])))


# Q3 — Generator expression
# Create a generator expression that produces cubes
# for numbers = [1, 2, 3, 4].
# Convert it to a list and print it.

numbers = [1,2,3,4]

cube_generator = (n ** 3 for n in numbers)

cube_list = list(cube_generator)
print(cube_list)


# Q1
# Write a generator countdown(n).
# Yield values from n down to 1.
# Example: list(countdown(4)) → [4, 3, 2, 1]

def countdown(n):
    while n >= 1:
        yield n
        n = n - 1
print(list(countdown(4)))


# Q2
# Write a generator positive_numbers(numbers).
# Yield only positive numbers from the given list.
# Example input: [-2, 3, 0, 5, -1]
# Expected: [3, 5]

def positive_numbers(numbers):

    for num in numbers:
        if num > 0:
            yield num
print(list(positive_numbers([-2,3,0,5,-1])))


# Q3
# Write a generator name_lengths(names).
# Yield the length of every name.
# Example input: ["AI", "Python", "Developer"]
# Expected: [2, 6, 9]

def name_lengths(names):
    
    for name in names:
        length = len(name)
        yield length
print(list(name_lengths(["AI", "Python", "Developer"])))

# Q4
# Create a generator expression that yields
# numbers divisible by 3 from:
numbers = [1, 3, 4, 6, 8, 9, 12]

# Convert it to a list and print it.
num_generator = (num for num in numbers if num % 3 == 0 )

num_list = list(num_generator)
print(num_list)


# Q5
# Create a generator expression for squares of:
numbers = [1, 2, 3, 4, 5]

# Use sum() directly on the generator.
# Expected result: 55

num_square = sum(num ** 2 for num in numbers)
print(num_square)



#7. Real-World Mini Project — Order Processing Stream



def high_value_orders(orders):

    for order in orders:
        if order >= 1000:
            yield order


orders = [350, 1200, 750, 2500, 999, 1800]
for order in high_value_orders(orders):
    commission = order * 0.10
    print(f"Order: {order} | Commission: {commission}")




# Q9
# Write a generator odd_numbers(n).
# It should yield all odd numbers from 1 to n.
# Example: list(odd_numbers(8)) → [1, 3, 5, 7]


def odd_numbers(n):
    for num in range(1, n + 1):
            if num % 2 != 0:
                yield num
print(list(odd_numbers(8)))


# Q10
# Write a generator word_upper(words).
# It should yield every word in uppercase.

def word_upper(words):
    for word in words:
        yield word.upper()

words = ["python", "generator", "code"]

for upper_word in word_upper(words):
    print(upper_word)


# Q11
# Create a generator expression that yields squares
# of only even numbers from this list.
numbers = [1, 2, 3, 4, 5, 6]

# Convert it to a list and print it.

number_generator = (num ** 2 for num in numbers)

number_list = list(number_generator)
print(number_list)

