



#============================================================

"""
# Q1
# Write a recursive function countdown(n)
# It should print n down to 1.
# Example: countdown(4) prints 4, 3, 2, 1

def countdown(n):
    if n == 0:
        return
    
    print(n)
    countdown(n - 1)
countdown(4)


# Q2
# Write a recursive function find_sum(n)
# It should return the sum from n down to 1.
# Example: find_sum(4) returns 10

def find_sum(n):
    if n == 0:
        return 0
    
    return n + find_sum(n - 1)
print(find_sum(4))


# Q3
# Write a recursive function factorial(n)
# Example: factorial(5) returns 120

def fectorial(n):
    if n == 0:
        return 1
    
    return n * fectorial(n - 1)
print(fectorial(5))
"""
#----------------------------------------------------------------------------
# Q1
# Write a recursive function count_up(n).
# It should print numbers from 1 to n.
# Example: count_up(5)
# Output: 1 2 3 4 5

def count_up(n):
    if n == 0:
        return 0
    
    count_up(n - 1)
    print(n)
count_up(5)


# Q2
# Write a recursive function sum_even(n).
# It should return the sum of all even numbers from n down to 0.
# Example: sum_even(6)
# Result: 12  (6 + 4 + 2 + 0)

def sum_even(n):
    if n == 0:
        return 0
    
    if n % 2 == 0:
        return n + sum_even(n - 2)
    else:
        return n + sum_even(n - 1)
print(sum_even(6))


# Q3
# Write a recursive function multiply_numbers(n).
# It should return multiplication from n down to 1.
# Example: multiply_numbers(4)
# Result: 24

def multiply_numbers(n):
    if n == 0:
        return 1
    
    return n * multiply_numbers(n - 1)
print(multiply_numbers(4))

# Q4
# Write a recursive function count_digits(number).
# It should return how many digits are in a positive integer.
# Example: count_digits(12345)
# Result: 5
def count_digit(n):
    if n < 10:
        return 1
    
    return 1 + count_digit(n // 10)
print(count_digit(12345))


# Q5
# Write a recursive function reverse_text(text).
# It should return the reversed string.
# Example: reverse_text("Python")
# Result: "nohtyP"

def reverse_text(text):
    if len(text) <= 1:
        return text
    
    return reverse_text(text[1:]) + text[0]
print(reverse_text("Python"))


# Q6
# Write the fibonacci(n) function.
# Test it with fibonacci(7).
# Expected result: 13

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(7))



"""
#Exercise 1 — Countdown
def countdown(n):
    if n == 0:
        return
    
    print(n)
    countdown(n - 1)
countdown(5)


#Exercise 2 — Count Up

def countup(n):
    if n == 0:
        return 
    
    countup(n - 1)
    print(n)
countup(5)


#Exercise 3 — Print a Message Multiple Times

def print_message(n):
    if n == 0:
        return
    
    print("Hello Python")
    print_message(n - 1)
    
print_message(3)


#Exercise 4 — Sum from 1 to N
def sum_number(n):
    if n == 0:
        return 0
    return n + sum_number(n - 1)
print(sum_number(5))
"""


"""#Recursion — Mixed Practice
#Exercise 1 — Even Numbers

def even_num(n):
    if n < 2:
        return 
    
    print(n)
    even_num(n - 2)
even_num(10)


#Exercise 2 — Factorial

def factorial(n):
    if n == 0:
        return 1
    
    return n * factorial(n - 1)
print(factorial(5))


#Exercise 3 — Power

def power(base, exponent):
    if exponent == 0:
        return 1
    
    else:
        return base * power(base, exponent - 1)
print(power(2, 3))


#Exercise 4 — Reverse Counting With a Twist

def countdown_message(n):
    if n == 0:
        print("Go!")
        return
    
    print(n)
    countdown_message(n - 1)

countdown_message(5)


#Exercise 5 — Sum of Even Numbers

def sum_even(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return n + sum_even(n - 2)
print(sum_even(10))


#Exercise 6 — Recursive Digit Count

def digit_count(n):
    if n < 10:
        return 1 
    
    return 1 + digit_count(n // 10)
print(digit_count(12345))


#Exercise 7 — Challenge

def sum_digits(n):
    if n < 10:
        return n
    
    return (n % 10) + sum_digits(n // 10)
print(sum_digits(1234))


#Exercise 8 — Factorial Function

def factorial(n):
    if n == 0:
        return 1
    
    return n * factorial(n - 1)
print(factorial(5))
print(factorial(3))
print(factorial(1))


#Exercise 9 — Factorial Function

def reverse_string(text):
    if len(text) <= 1:
        return text
    
    return text[-1] + reverse_string(text[:-1])
print(reverse_string("Python"))


#Exercise 10 — Count a Character

def count_characters(text, target):
    return text.count(target)
print(count_characters("banana", "a"))


#Exercise 11 — Find Maximum

def find_max(numbers):

    if len(numbers) == 1:
        return numbers[0]
    
    max_num = find_max(numbers[1:])

    if numbers[0] > max_num:
        return numbers[0]
    else:
        return max_num
    
numbers = [10,25,7,42,18]
print(find_max(numbers))


#Exercise 12 — Sum a List

def sum_list(numbers):

    if len(numbers) == 0:
        return 0
    
    else:
        return numbers[0] + sum_list(numbers[1:])
numbers = [10, 20, 30, 40]

print(sum_list(numbers))


#Exercise 13 — Palindrome

def is_palindrome(text):

    return text == text[::-1]

print(is_palindrome("madam"))
print(is_palindrome("level"))
print(is_palindrome("python"))


#Exercise 14 — Fibonacci

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(6))
"""






#revese number

def reverse_number(n,rev):
    if n == 0:
        return rev
    
    return reverse_number(n // 10, rev * 10 + n % 10)
print(reverse_number(1234, 0))


#Exercise 1 — Sum of Digits

def sum_digits(n):
    if n == 0:
        return 0
    
    return (n % 10) + sum_digits(n // 10) 
print(sum_digits(5728))
print(sum_digits(4062))
print(sum_digits(999))


#Exercise 2 — Count Digits

def count_digits(n):
    if n == 0:
        return 0
    
    return 1 + count_digits(n // 10)
print(count_digits(12345))
print(count_digits(72))
print(count_digits(9))


#Exercise 3 — Count Even Digits

def count_even_digits(n):
    if n == 0:
        return 0
    
    if (n % 10) % 2 == 0:
        return 1 + count_even_digits(n // 10)
    else:
        return count_even_digits(n // 10)
print(count_even_digits(572846))
print(count_even_digits(13579))
print(count_even_digits(2468))


#Exercise 4 — Count Odd Digits
def count_odd_digits(n):
    if n == 0:
        return 0
    
    if (n % 10) % 2 != 0:
        return 1 + count_odd_digits(n // 10)
    else:
        return count_odd_digits(n // 10)
print(count_odd_digits(583726))
print(count_odd_digits(2468))
print(count_odd_digits(13579))


#Exercise 5 — Sum of Even Digits

def sum_even_digits(n):
    if n == 0:
        return 0
    
    if (n % 10) % 2 == 0:
        return (n % 10) + sum_even_digits(n // 10)
    else:
        return sum_even_digits(n // 10)
print(sum_even_digits(583726))
print(sum_even_digits(2468))
print(sum_even_digits(13579))


#Exercise 6 — Sum of Odd Digits

def sum_odd_digits(n):
    if n == 0:
        return 0
    
    if (n % 10) % 2 != 0:
        return (n % 10) + sum_odd_digits(n // 10)
    else:
        return sum_odd_digits(n // 10)
print(sum_odd_digits(583726))
print(sum_odd_digits(2468))
print(sum_odd_digits(13579))


#Exercise 7 — Count Digits Greater Than 5

def count_greater_then_5(n):
    if n == 0:
        return 0
    
    if (n % 10) > 5:
        return 1 + count_greater_then_5(n // 10)
    else:
        return count_greater_then_5(n // 10)
print(count_greater_then_5(583726))
print(count_greater_then_5(12345))
print(count_greater_then_5(9876))


#Exercise 8 — Sum Digits Greater Than 5
def sum_greater_then_5(n):
    if n == 0:
        return 0
    
    if (n % 10) > 5:
        return (n % 10) + sum_greater_then_5(n // 10)
    else:
        return sum_greater_then_5(n // 10)

print(sum_greater_then_5(583726))
print(sum_greater_then_5(12345))
print(sum_greater_then_5(9876))


#Exercise 9 — Find Largest Digit

def largest_digits(n):
    if n == 0:
        return 0

    last_digit = n % 10
    largest_num = largest_digits(n // 10)

    if last_digit > largest_num:
        return last_digit
    else:
        return largest_num

print(largest_digits(583726))


#Exercise 10 — Find Smallest Digit

def smallest_digits(n):
    if n < 10:
        return n
    
    last_digit = n % 10
    smallest_num = smallest_digits(n // 10)

    if smallest_num < last_digit:
        return smallest_num
    else:
        return last_digit
print(smallest_digits(583726))


#Exercise 11 — Count a Specific Digit

def count_digit(n,target):
    if n == 0:
        return 0
    
    if (n % 10) == target:
        return 1 + count_digit(n // 10, target)
    else:
        return count_digit(n // 10, target)

print(count_digit(122333,3))
print(count_digit(122333, 2))
print(count_digit(55555,5))
print(count_digit(12345,9))


#Exercise 12 — Reverse Number

def reverse_number(n, rev):
    if n == 0:
        return rev
    
    return reverse_number(n // 10, rev * 10 + n % 10)
print(reverse_number(1234,0))
print(reverse_number(507, 0))
print(reverse_number(12321,0))


#Exercise 13 — Palindrome Number

def is_palindrome(n):
    original = n

    reversed_num = reverse_number(n,0)
    return original == reversed_num
print(is_palindrome(121))


#Exercise 14 — Product of Digits

def product_digits(n):
    if n == 0:
        return 1
    
    return (n % 10) * product_digits(n // 10)
print(product_digits(234))
print(product_digits(1234))
print(product_digits(505))


#Exercise 15 — Count Zero Digits

def count_zero_digits(n):
    if n == 0:
        return 0
    
    if (n % 10) == 0:
        return 1 + count_zero_digits(n // 10)
    else:
        return count_zero_digits(n // 10)
    
print(count_zero_digits(102030))
print(count_zero_digits(12345))
print(count_zero_digits(1001))


#Exercise 16 — Sum Digits at Even Positions

def sum_even_position_digits(n,position):
    if n == 0:
        return 0
    
    if position % 2 == 0:
        return (n % 10) + sum_even_position_digits(n // 10, position + 1)
    else:
        return sum_even_position_digits(n // 10, position + 1)
print(sum_even_position_digits(123456, 1))


#Final Mixed Challenge
#Exercise 17 — Number Analyzer

def number_analyzer(n):
    return n


def number_of_digits(n):
    if n == 0:
        return 0
    return 1 + number_of_digits(n // 10)


def sum_of_digits(n):
    if n == 0:
        return 0
    
    return (n % 10) + sum_of_digits(n // 10)


def largest_digit(n):
    if n == 0:
        return 0
    
    last_digit = n % 10
    largest_num = largest_digit(n // 10)

    if largest_num > last_digit:
        return largest_num
    else:
        return last_digit
    

def smallest_digit(n):
    if n < 10:
        return n
    
    last_digit = n % 10
    smallest_num = smallest_digit(n // 10)

    if smallest_num < last_digit:
        return smallest_num
    else:
        return last_digit


def even_digit_count(n):
    if n == 0:
        return 0
    
    if (n % 10) % 2 == 0:
        return 1 + even_digit_count(n // 10)
    else:
        return even_digit_count(n // 10)


def odd_digit_count(n):
    if n == 0:
        return 0
    
    if (n % 10) % 2 !=0:
        return 1 + odd_digit_count(n // 10)
    else:
        return odd_digit_count(n // 10)


def reverse_number(n, rev):
    if n == 0:
        return rev
    
    return reverse_number(n // 10, rev * 10 + n % 10)


def is_palindrome(n):
    original = n

    reversed_num = reverse_number(n, 0)
    return reversed_num == original



print("---------------NUMBER ANALYZER------------------")
print("Original Number: ",number_analyzer(583726))
print("Number Of Digits: ",number_of_digits(583726))
print("Sum Of Digits: ",sum_of_digits(583726))    
print("Largest Digit: ",largest_digit(583726))
print("Smallest Digit: ",smallest_digit(583726))
print("Even Digit Count: ",even_digit_count(583726))
print("Reverse Number: ",reverse_number(583726, 0))
print("Odd Digit Count: ",odd_digit_count(583726))
print("Palindrome Or Not: ", is_palindrome(583726))
