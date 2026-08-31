                    #=================================================================
                                #Phase 2 — Intermediate Python

                                #Topic 1 — File Handling
                    #=================================================================



#=============================== basic write and read=========================================


"""#"w" Write
file = open("intro.txt","w")

file.write("Name: Hardik\n")
file.write("Fav Language: Python\n")
file.write("Goal: Software Engineer\n")

file.close()

#"a" append 
file = open("intro.txt", "a")

file.write("\nLearning: File Handling")
file.close()

#"r" read 
file = open("intro.txt", "r")

data = file.read()
print(data)
file.close()"""


#2

file = open("message.txt", "w")
file.write("Python is powerful\n")
file.write("File handling is useful")

file.close()

file = open("message.txt", "r")
data = file.read()
print(data)

file.close()


#3

# name = input("Enter Name :")
# notes = input("Enter Notes :")

# file = open("notes.txt","w")
# file.write(f"Name : {name} \n")
# file.write(f"Notes : {notes}\n")

# file.close()

# file = open("notes.txt", "r")

# data = file.read()
# print(data)
# file.close()


#Exercise 1 — Student Information

# name = input("Enter Your Name :")
# age = int(input("Enter Your Age :"))
# course = input("Enter Your Course :")

# file = open("student.txt", "w")

# file.write(f"Name : {name}\n")
# file.write(f"Age : {age} \n")
# file.write(f"Course : {course}\n")

# file.close()

# file = open("student.txt", "r")

# data = file.read()
# print(data)
# file.close()

#Exercise 2 — Daily Expense Saver

# expense_name = input("Enter Expense Name :")
# expense_amount = int(input("Enter Expense Amount :"))

# file = open("expenses.txt", "a")

# file.write(f"{expense_name} : {expense_amount}\n")
# file.close()


# file = open("expenses.txt", "r")

# data = file.read()
# print(data)

# file.close()


#Exercise 3 — Read and Count

# file = open("characters.txt", "w")

# file.write("I am Learning Python and Aspiring to Software Engineer")
# file.close()


# file = open("characters.txt", "r")

# data = file.read()
# print(data)
# print(len(data))

# file.close()


#Exercise 4 — Simple Notes App

# note = input("Enter Note :")

# file = open("my_notes.txt", "a")
# file.write(f"Note :{note}\n")
# file.close()

# file = open("my_notes.txt", "r")
# data = file.read()
# print(data)
# file.close()




                                #==============================================
                                        #USING WITH OPEN () AS FILE:
                                #==============================================

# with open("practice.txt", "w") as file:
#     file.write("Python File Handling\n")
#     file.write("Learning Software Engineering\n")

# with open("practice.txt", "r") as file:
#     data = file.read()
#     print(data)


#2

with open("students.txt", "w") as file:
    file.write("Hardik\n")
    file.write("Rahul\n")
    file.write("Amit\n")
    file.write("Priya\n")

with open("students.txt", "r") as file:
    data = file.read()
    print(data)

with open("students.txt","r") as file:
    first_line = file.readline()
    second_line = file.readline()
    print(first_line, end="")
    print(second_line, end="")


#using readlines()
with open("students.txt", "r") as file:
    students = file.readlines()
    print(students)


#Student List Reader

# with open("students.txt", "r") as file:
#     all_students = file.readlines()

#     for student in all_students:
#         print(student, end="")

#

with open("students.txt", "r") as file:
    all_students = file.readlines()
    count = 0
    for student in all_students:
        count += 1
        print(f"{count}.{student}",end="")


#create file using "x"
# with open("profile.txt", "x") as file:
#     file.write("Name: Hardik\n")
#     file.write("Learning: Python\n")
#     file.write("Goal: Software Engineer\n")
 
try:
    with open("project.txt", "x") as file:
        file.write("My Python Software Engineer Journey")
except FileExistsError:
    print("File Already Exists!!")



#Practice 1 — Safe File Reader
try:
    with open("abc.txt", "r") as file:
        data = file.read()
        print(data)
except FileNotFoundError:
    print("abc File Not Found!")


#Concept Practice — Practice 2
try:
    with open("data.txt", "r") as file:
        data = file.read()
        print(data)
except FileNotFoundError:
    print("data file not found")
except PermissionError:
    print("Permission Denied!!")


#Mixed Practice — Safe File Creator
# try:
#     filename = input("Enter File Name :")
#     text = input("Enter Text :")

#     with open(filename, "x") as file:
#         file.write(f"{text}\n")
#     print("File Created Successfully")
# except FileExistsError:
#     print("File Already Exists!")



#Concept Practice — UTF-8=================

with open("language.txt", "w",encoding="utf-8") as file:
    file.write("English: Hello\n")
    file.write("German: Hallo\n")
    file.write("Gujarati: નમસ્તે\n")

with open("language.txt", "r", encoding="utf-8") as file:
    data = file.read()
    print(data)


#File Handling — File Cursor: tell() and seek()

# with open("demo.txt", "w") as file:
#     file.write("Python")

# with open("demo.txt", "r") as file:
#     first = file.read(2)
#     print(first)

#     print(file.tell())

#     file.seek(0)

#     second = file.read(2)
#     print(second)


#Mixed Practice

# with open("mixed.txt", "w") as file:
#     file.write("SoftwareEngineer")

# with open("mixed.txt", "r") as file:
#     first_read = file.read(8)
#     print(first_read)

#     print(file.tell())

#     file.seek(0)

#     second_read = file.read(8)
#     print(second_read)



#Real-World Mini Project — Student Notes Manager

def add_note():
    student_name = input("Enter Student Name: ")
    note = input("Enter Note: ")

    with open ("student_notes.txt", "a", encoding="utf-8") as file:
        file.write(f"Student :{student_name}\n")
        file.write(f"Note: {note}\n")
        file.write("---------------------------\n")
    print("Note Saved Successfully!")

def view_notes():
    try:
        with open("student_notes.txt", "r", encoding="utf-8") as file:
            data = file.read()
            print(data)
    except FileNotFoundError:
        print("File Not Found!") 

while True:
        print("\n========== STUDENT NOTES MANAGER =========")
        print("1. Add Student Note")
        print("2. View All Notes")
        print("3. Exit")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid Choice..!!!")