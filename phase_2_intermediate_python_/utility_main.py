



                                                        #Exercise 3 — Utility Package Challenge

from utility_package.number_tools import is_even, find_max
from utility_package.text_tools import count_words, to_upper

number = int(input("Enter Number: "))
numbers = [10,20,30,40,50]
sentense = input("Enter Sentense: ")

print("Number Even:",is_even(number))
print("Maximum: ",find_max(numbers))
print("Total Words: ",count_words(sentense))
print("Converted To Upper: ",to_upper(sentense))
