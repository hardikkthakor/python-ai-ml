



def check_result(marks):
    if marks >=40:
        return "Pass"
    else:
        return "Fail"

def get_grade(marks):
    if marks >= 90:
        return "Grade A"
    elif marks >= 75:
        return "Grade B"
    elif marks >= 60:
        return "Grade C"
    elif marks >= 40:
        return "Grade D"
    else:
        return "Grade F"
