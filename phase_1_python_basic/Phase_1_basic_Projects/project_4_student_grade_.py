

                            #=============================================
                                #PROJECT-4 STUDENT GRADE CALCULATOR
                            #=============================================
try:
    student = {
        "Hardik": 91,
        "Bhoomi": 99,
        "Neha": 31,
        "Priya": 21,
        "Neel": 40,
        "Krish": 32

    }
    
    max_marks = 0
    min_marks = 100
    for key, value, in student.items():

        print(key, ":", value)

        if value > max_marks:
            max_marks = value
        if value < min_marks:
            min_marks = value
        
    print("Highest Marks :",max_marks)
    print("Lowest Marks :",min_marks)

    total = sum(student.values())
    print("Total Marks :",total) 

    avg = total / len(student)
    print("Average Marks :",avg )

    pass_count = 0
    fail_count = 0

    for marks in student.values():
        if marks >= 40:
            pass_count +=1
        else:
            fail_count += 1

    print("Pass Students :", pass_count)
    print("Fail Students :", fail_count)

    
    search = input("Enter Student Name :")
    if search in student:
         print(search,":", student[search])
    else:
        print("Student Not Found")
            
except ValueError:
    print("Invalid Input")
