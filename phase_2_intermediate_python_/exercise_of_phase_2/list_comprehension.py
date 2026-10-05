

#1. The Even Number Extractor
even_numbers = [
    num for num in range(1,21) 
    if num % 2 == 0
]
print(even_numbers)

#2. Uppercase Converter
words = ["apple", "banana", "cherry", "date"]

uppercase_words = [word.upper() for word in words]
print(uppercase_words)

#3. Length Checker
words = ["apple", "banana", "cherry", "date"]

words_length = [len(word) for word in words]
print(words_length)

#4. Vowel Filter
characters = ['a', 'b', 'c', 'd', 'e', 'f', 'i', 'o']
vowels = "aeiou"

vowels_char = [char for char in characters if char in vowels]
print(vowels_char)

#5. Multiples of 3
multiples = [num for num in range(1,31) if num % 3 ==0]
print(multiples)

#6. The Parity Labeler
even_odd = [
    "Even" if num % 2 == 0
      else "Odd" 
      for num in range(1,11)
      ]
print(even_odd)
