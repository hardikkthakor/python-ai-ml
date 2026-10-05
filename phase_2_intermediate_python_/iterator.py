


                    #==================================================================================
                                                            #iterator
                    #==================================================================================

# Q1 — 
# Create an iterator from:
numbers = [100, 200, 300]

# Print its first two values using next().
it = iter(numbers)
print(next(it))


# Q2 —
# Create an iterator from this dictionary's keys,
# then print the first key.
student = {
    "name": "Hardik",
    "age": 20,
    "city": "Delhi"
}

it = iter(student)
print(next(it))


# Q1
# Create an iterator from this tuple.
# Print all three values using next().
skills = ("Python", "SQL", "Git")

iterator = iter(skills)

print(next(iterator))
print(next(iterator))
print(next(iterator))


# Q2
# Create an iterator from this string.
# Print its first four characters using next().
word = "Code"

it = iter(word)

print(next(it))
print(next(it))
print(next(it))
print(next(it))


# Q3
# Create an iterator from this list.
# Take the first value with next(), then print the remaining values as a list.
numbers = [10, 20, 30, 40]

it = iter(numbers)

print(next(it))
print(list(it))


# Q4
# Use a for loop to print every item from this iterator.
colors = ["Red", "Blue", "Green"]

for color in colors:
    it = iter(color)
    print(color)



#-----------------------------------------------
#. Real-World Mini Project — Task Queue Processor

tasks = [
    "Reply to customer",
    "Fix login bug",
    "Review pull request",
    "Deploy update"
]

it = iter(tasks)

print(next(it))
print(next(it))
print(list(it))