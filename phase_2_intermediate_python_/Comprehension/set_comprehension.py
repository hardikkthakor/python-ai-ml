

#Q1 — Unique Squares
numbers = [1, 2, 2, 3, 3, 4]

squares = {
    num ** 2 for num in numbers
    }
print(squares)

#Q2 — Unique Even Numbers
numbers = [1, 2, 2, 3, 4, 4, 5, 6]

even_num = {
    num for num in numbers if num % 2 == 0
}
print(even_num)

#Q3 — Unique Word Lengths
words = ["AI", "Python", "ML", "Data", "Code", "Java"]

lengths_word = {
    len(word) for word in words
    }
print(lengths_word)

#Q4 — Positive or Negative
numbers = [-5, -2, 0, 3, 7]

pos_neg = {
    "Positive" if num > 0 else "Negative" if num < 0 else "Zero"
    for num in numbers
}
print(pos_neg)


#Q5 — Unique Uppercase Names
names = ["hardik", "rahul", "Hardik", "python", "PYTHON"]

uppercase_names = {
    name.upper() for name in names
}
print(uppercase_names)


#Q6 — Unique Positive Squares
numbers = [-2, 3, 3, 4, -5, 4, 0]
square_pos = {
    num ** 2 for num in numbers if num > 0
}
print(square_pos)


#Q7 — Unique First Letters
words = ["Python", "Programming", "Data", "Developer", "AI", "Artificial"]

unique_first_letters = {
    word[0].upper() 
    for word in words
}
print(unique_first_letters)


#Q8 — Discount Categories
prices = [500, 1200, 800, 1500, 1200, 500]

discount = {
    "Discount" if price >=1000 else "Regular"
    for price in prices
}
print(discount)


#Exercise 9 — Double and Remove Duplicates
numbers = [1, 2, 2, 3, 4, 4, 5]

double = {
    num * 2 for num in numbers
}
print(double)

#Exercise 10 — Unique Odd Numbers
numbers = [1, 2, 3, 3, 4, 5, 5, 7, 8]

odd_num = {
    num for num in numbers 
    if num % 2 != 0
    }
print(odd_num)


#Exercise 11 — Unique Word Lengths
words = ["Python", "Java", "AI", "Data", "ML", "Code"]

length_words = {
    len(word) for word in words
} 
print(length_words)


#Exercise 12 — Positive Squares
numbers = [-3, 2, 4, -1, 2, 5, 0, 4]

positive_square = {
    num ** 2 for num in numbers if num > 0
}
print(positive_square)


#Exercise 13 — Clean Unique Names
names = ["hardik", "", "Hardik", "  ", "rahul", "RAHUL", "python"]

cleaned_unique_name = {
    name.upper() for name in names if name.strip() != ""
}
print(cleaned_unique_name)


#Exercise 14 — Number Status
numbers = [-5, -2, 0, 3, 7, -1, 0, 10]

check_num = {
    "Positive" if num > 0 else "Negative" if num < 0 else "Zero"
    for num in numbers
}
print(check_num)


#Exercise 15 — Grade Categories
marks = [95, 82, 67, 45, 39, 20, 95, 82]

grade_categories = {
    "Excellent" if mark >=80
    else "Good" if mark >=60
    else "Pass" if mark >=40
    else "Fail"
    for mark in marks
}
print(grade_categories)


#Exercise 16 — First Letters

languages = [
    "Python",
    "Programming",
    "Java",
    "JavaScript",
    "Artificial Intelligence",
    "AI"
]

unique_first_letters = {
    language[0].upper() for language in languages
}
print(unique_first_letters)



#Mini Project — Unique Skills Analyzer

skills = [
    "python",
    "Python",
    "AI",
    "machine learning",
    "AI",
    "data science",
    "Python",
    "",
    "  ",
    "Machine Learning"
]

unique_skills = {
    skill.strip().upper() for skill in skills 
    if skill.strip() != ""
}

long_skills = {
    skill.strip().upper() 
    for skill in skills 
    if skill.strip() != "" and len(skill.strip()) > 5
}

skill_categories = {
    
    "SHORT" if len(skill.strip()) <= 5
    else "LONG"
    for skill in skills
    if skill.strip() != ""
}

print("===== UNIQUE SKILLS ANALYZER =====")

print("Original Skills: \n",skills)
print("Unique Skills: \n", unique_skills)
print("Long Skills: \n",long_skills)
print("Skill Categories: \n", skill_categories)