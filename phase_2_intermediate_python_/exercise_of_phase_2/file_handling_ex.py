



#Exercise 1 — Personal Profile

with open("profile.txt", "w") as file:
    file.write("Name: hardik\n")
    file.write("Language: Python\n")
    file.write("Goal: SOftware Engineer\n")

with open("profile.txt", "r") as file:
    data = file.read()
    print(data)


#Exercise 2 — Daily Notes App

# note = input("Enter Your Note :")

# with open("daily_notes.txt", "a") as file:
#     file.write(f"\n{note}")

# with open("daily_notes.txt", "r") as file:
#     data = file.read()
#     print(data)


#Exercise 3 — Number Students

with open("friends.txt", "w") as file:
    file.write("Hardik\n")
    file.write("Bhoomi\n")
    file.write("Neha\n")
    file.write("Anjali\n")

with open("friends.txt", "r") as file:
    data = file.readlines()
    count = 0
    for friend in data:
        count += 1
        print(f"{count}.{friend}",end="")


#Exercise 4 — Safe File Reader
# try:
#     file_name = input("Enter File Name :")
#     with open(file_name, "r") as file:
#         data = file.read()
#         print(data)
# except FileNotFoundError:
#     print("File Not Found!!")


#Exercise 5 — Safe File Creator
# try:
#     file_name = input("Enter File Name:")
#     text = input("Enter Text:")

#     with open(file_name, "x") as file:
#         file.write(text)
#     print("File Created Successfully!!")
# except FileExistsError:
#     print("File Already Exists!!")


#Exercise 6 — Multi-Language File

# with open("lang.txt", "w", encoding="utf-8") as file:
#     file.write("English: Hello\n")
#     file.write("Gujarati: નમસ્તે\n")
#     file.write("German: Hallo\n")
#     file.write("Emoji: 🚀\n")

# with open("lang.txt", "r", encoding="utf-8") as file:
#     data = file.read()
#     print(data)

#Exercise 7 — File Cursor Practice

# with open("cursor.txt", "w") as file:
#     file.write("PythonProgramming")

# with open("cursor.txt", "r") as file:
#     first_read = file.read(6)
#     print(first_read)

#     print(file.tell())

#     file.seek(0)
#     second_read = file.read(6)
#     print(second_read)

#Exercise 8 — Student Notes Manager

# student_name = input("Student: ")
# notes = input("Note: ")
# with open("student_notes.txt", "a", encoding="utf-8") as file:
#     file.write(f"Student: {student_name}\n")
#     file.write(f"Note: {notes}\n")
#     file.write("-------------------\n")

# with open("student_notes.txt", "r", encoding="utf-8") as file:
#     data = file.read()
#     print(data)



#Q10 — Safe Notes App
# note = input("Enter Note: ")
# with open("notes.txt","a", encoding="utf-8") as file:
#     file.write(f"{note}\n")

# with open("notes.txt", "r", encoding="utf-8") as file:
#     data = file.read()
#     print(data)

#Q11 — Safe File Reader
# try:
#     file_name = input("Enter File Name: ")

#     with open(file_name, "r", encoding="utf-8") as file:
#         data = file.read()
#         print(data)
# except FileNotFoundError:
#     print("File Not Found!!")

#Q12 — Final Challenge

# def add_text():
#         text = input("Enter Text: ")

#         with open("data.txt", "a", encoding="utf-8") as file:
#             file.write(f"{text}\n")
        
#         print("Text Added Successfully!!!")

# def view_file():
#     try:
#         with open("data.txt", "r", encoding="utf-8") as file:
#             data = file.read()
#             print(data)
    
#     except FileNotFoundError:
#         print("File Not Found!!")

# while True:
#     print("===========File Manager============")
#     print("1.Add Text ")
#     print("2.View File ")
#     print("3.Exit ")


#     choice = input("Enter Your Choice: ")

#     if choice == "1":
#         add_text()
#     elif choice == "2":
#         view_file()
#     elif choice == "3":
#         print("Exiting..")
#         break
#     else:
#         print("Invalid Choice")


#Q10 — Final Practical Challenge

import random
import datetime

messages = [
    "I am Learning Python",
    "I want to become a Software Engineer",
    "Built My Career Well"
]

selected = random.choice(messages)
print(selected)

now = datetime.datetime.now()
print(now.strftime("%d %b, %Y")) 
