#1
def student(name):
    print("Student Name :", name)

student("Hardik")
student("Rahul")
student("Aman")

#2

def dream(country):
    print("My Dream Country Is :", country)

dream("Germany")
dream("Japan")
dream("Canada")

#3

def language(lang):
    print("I love :", lang)

language("Python")
language("Java")
language("C++")


#4 with two parameters
def student(name, age):
    print("Name :", name)
    print("Age :", age)

student("Hardik", 24)
student("Rahul", 22)

#5

def marks(name, score):
    print("Student :", name)
    print("Marks :",score)

marks("Hardik", 95)
marks("Aman", 88)
marks("Priya", 91)

#6 

def dream(name, country):
    print(name, "Wants To Go To", country)

dream("Hardik","Germany")
dream("Rahul","Japan")
dream("Aman", "Canada")


                                    #7 ADDITION

def add(a,b):
    return a + b

result = add(15,20)
print(result)

                                        #8 
def positive(number):
    if number > 0:
        return "Positive"
    else:
        return "Negative"
print(positive(4))

                            #9 CHECK VOTING ELIGIBILITY

def voting(age):
    if age >=18:
        return "Eligible"
    else:
        return "Not Eligible"
print(voting(18))


                            #10 RETURN LARGEST NUMBER 

def largest(a,b):
    if a > b:
        return a
    else:
        return b
print(largest(9,4))

                                    #11

def welcome(name = "Buddy"):
    print("Welcome", name)
welcome()
welcome("Hardik")

                                    #12

def country(place = "Germany"):
    print("Dream Country :", place)
country()
country("Japan")
country("Canada")

def multipy(number = 5):
    return number * 10
print(multipy())
print(multipy(8))
