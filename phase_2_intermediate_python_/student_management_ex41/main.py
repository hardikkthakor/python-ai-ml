


#FINAL — Full Phase 1 + Phase 2 Project
#Exercise 41 — Student Management & Analysis System

students = []

class InvalidStudentDataError(Exception):
    pass


def get_valid_age():
    while True:
        try:
            age = int(input("Enter Age: "))

            if age < 0:
                raise InvalidStudentDataError("Age must be greater then 0")
            
            return age
        
        except ValueError:
            print("Invalid Input, Age Must be a number..")
        except InvalidStudentDataError as e:
            print(e)

def get_valid_marks():
    while True:
        try:
            marks = float(input("Enter Marks(0-100): "))

            if marks < 0 or marks > 100:
                raise InvalidStudentDataError("Marks Must be between 0-100..!!")
            
            return marks
        except ValueError:
            print("Invalid Input!!, Marks Must be number.")
        except InvalidStudentDataError as e:
            print(e)
        
def get_skills():
    while True:
            
            skills_input = input("Enter Skills Separated by comma: ")

            if not skills_input:
                print("Please Enter Atleast One Skill..")
                continue
            
            skills = [
                skill.strip()
                for skill in skills_input.split(",")
                if skill.strip()
            ]
            if skills:
                return skills
            print("Invalid Skills!")
        
def add_student():
    print("\n================ ADD STUDENT ===============")

    name = input("Enter Name: ")

    while not name:
        print("Name Cannot be empty")
        name = input("Enter Name: ")

    age = get_valid_age()

    course = input("Enter Course: ")
    while not course:
        print("course cannot be empty..!")
        course = input("Enter Course: ")

    marks = get_valid_marks()

    skills = get_skills()

    student = {
        "name": name,
        "age": age,
        "course": course,
        "marks": marks,
        "skills": skills
    }

    students.append(student)
    print("\nStudent Added Successfully..!")


def view_student():
    print("\n============ ALL STUDENTS ============")

    if not students:
        print("No Student Available!")
        return
    
    for index, student in enumerate(students, start=1):

        print(f"\n Student {index}")
        print("-" * 35)
        print(f"Name      : {student["name"]}")
        print(f"Age       : {student["age"]}")
        print(f"Course    : {student["course"]}")
        print(f"Marks     : {student["marks"]}")
        print(f"Skills    : {", ".join(student["skills"])}")

def search_student():
    print("\n========== SEARCH STUDENT ==========")

    if not students:
        print("No students available.")
        return

    search_name = input("Enter student name: ").strip().lower()

    found_students = [
        student
        for student in students
        if search_name in student["name"].lower()
    ]

    if not found_students:
        print("Student not found.")
        return

    print("\nMatching students:")

    for index, student in enumerate(found_students, start=1):
        print(f"\nStudent {index}")
        print(f"Name   : {student['name']}")
        print(f"Age    : {student['age']}")
        print(f"Course : {student['course']}")
        print(f"Marks  : {student['marks']}")
        print(f"Skills : {', '.join(student['skills'])}")


def analyze_students():
    print("\n============= STUDENT ANALYSIS ==============")

    if not students:
        print("No student available for analysis.")
        return
    total_students = len(students)

    marks = list(map(lambda student: student["marks"], students))

    average_marks = sum(marks) / total_students

    highest_marks = max(marks)
    lowest_marks = min(marks)

    passed_students = list(filter(lambda student: student["marks"] >= 40, students))

    failed_students = list(filter(lambda student: student["marks"] < 40, students))

    unique_course = {
        student["course"] 
        for student in students 
    }

    unique_skills = {
        skill.strip()
        for student in students
        for skill in student["skills"]
    }


    print(f"\nTotal students   : {total_students}")
    print(f"Average marks      : {average_marks}")
    print(f"Highest marks      : {highest_marks}")
    print(f"Lowest marks       : {lowest_marks}")
    print(f"Passed students    : {len(passed_students)}")
    print(f"Failed students    : {len(failed_students)}")

    print("\n Unique courses:")
    for course in sorted(unique_course):
        print(f"- {course}")

    
    while True:
        try:
            x = float(input("\nEnter Marks to find students above x: "))

            students_above_x = [student for student in students if student["marks"] > x]
            break

        except ValueError:
            print("Please Enter a valid number.")

        print(f"\nStudent With Marks > {x}:")

        if students_above_x:
            for student in students_above_x:
                print(f"- {student["name"]}"f"({student["marks"]} marks)")
        else:
            print("No Student Found.")

        
def save_students():
    print("\n============ SAVE STUDENTS =============")

    if not students:
        print("No Student Available.")
        return
    
    try:
        with open("students.txt", "w", encoding="utf-8") as file:

            for student in students:
                skills = ",".join(student["skills"])

                line = (
                    f"{student["name"]}|"
                    f"{student["age"]}|"
                    f"{student["course"]}|"
                    f"{student["marks"]}|"
                    f"{skills}\n"
                )

                file.write(line)
            print("Students Save Successfully!")
    except PermissionError:
        print("Permission Denied. Cannot Write to the file.")
    
    except OSError as error:
        print(error)
    
def load_students():
    print("\n========== LOAD STUDENTS ==========")

    try:
        with open("students.txt", "r", encoding="utf-8") as file:

            loaded_students = []

            for line_number, line in enumerate(file, start=1):

                line = line.strip()

                if not line:
                    continue

                try:
                    parts = line.split("|")

                    if len(parts) != 5:
                        raise InvalidStudentDataError(
                            f"Invalid record on line {line_number}."
                        )

                    name = parts[0]
                    age = int(parts[1])
                    course = parts[2]
                    marks = float(parts[3])

                    skills = [
                        skill.strip()
                        for skill in parts[4].split(",")
                        if skill.strip()
                    ]

                    student = {
                        "name": name,
                        "age": age,
                        "course": course,
                        "marks": marks,
                        "skills": skills
                    }

                    loaded_students.append(student)

                except (ValueError, InvalidStudentDataError) as error:
                    print(
                        f"Skipping invalid line "
                        f"{line_number}: {error}"
                    )

            # Replace existing data instead of duplicating it
            students.clear()
            students.extend(loaded_students)

        print(
            f"{len(students)} student(s) loaded successfully!"
        )

    except FileNotFoundError:
        print(
            "students.txt not found. "
            "Save students first."
        )

    except PermissionError:
        print("Permission denied. Cannot read the file.")

    except OSError as error:
        print(f"File error: {error}")

def main():

    while True:

        print("\n========== STUDENT MANAGEMENT SYSTEM ==========")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Analyze Students")
        print("5. Save to File")
        print("6. Load from File")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            view_student()

        elif choice == "3":
            search_student()

        elif choice == "4":
            analyze_students()

        elif choice == "5":
            save_students()

        elif choice == "6":
            load_students()

        elif choice == "7":
            print("\nExiting program...")
            break

        else:
            print("Invalid choice! Please enter 1-7.")

if __name__ == "__main__":
    main()
