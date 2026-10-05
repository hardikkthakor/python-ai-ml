


import numpy as np
from colorama import Fore,Style

user_input = input("Enter Number: ")
numbers = [float(num) for num in user_input.split()]
num_array = np.array(numbers)

print(Fore.RED + "===== NUMBER ANALYZER =====\n")

print(Fore.WHITE + f"Numbers: {num_array}")

total = sum(num_array)
print(Fore.RED + f"Total: {total}")

average = total / len(num_array)
print(Fore.RED + f"Average: {average}")

maximum = max(num_array)
print(Fore.RED + f"Max: {maximum}")

minimum = min(num_array)
print(Fore.RED + f"Min: {minimum}")

print(Style.RESET_ALL)