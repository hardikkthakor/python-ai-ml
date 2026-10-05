



def calculate_percentage(marks):
    return sum(marks) / len(marks)

def get_result(percentage):
    if percentage >= 40:
        return "Pass"
    else:
        return "Fail"
