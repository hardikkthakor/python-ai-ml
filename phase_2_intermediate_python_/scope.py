


#=============================================================
                    #SCOPE — CONCEPT PRACTICE
#=============================================================

#Exercise 1 — Local Variable
"""
def student_details():
    name = "Hardik"
    age = 24

    print(name)
    print(age)
student_details()


#Exercise 2 — Global Variable

company = "ABC Technologies"

def show_company():
    print(company)
show_company()


#Exercise 3 — Local vs Global

name = "Hardik"

def show_name():
    name = "Rahul"
    print(name)
show_name()
print(name)


#Exercise 4 — Fix the Global Variable

score = 50

def update_score():
    global score
    score = 100

update_score()
print(score)


#Exercise 5 — Nested Function

def outer():
    number = 10
    def inner():
        print(number)
    inner()
outer()


#Exercise 6 — nonlocal

def counter():
    count = 0

    def increase():
        nonlocal count
        count += 1
        pass

    increase()
    increase()
    print(count)
counter()


#Exercise 7 — LEGB Challenge

x = 100

def outer():
    x = 200
    
    def inner():
        x = 300

        print(x)
    inner()
    print(x)
outer()
print(x)
"""


#Exercise 1 — Local + Global
"""name = "Hardik"

def show_name():
    name = "Rahul"
    print(name)
show_name()
print(name)


#Exercise 2 — Global Modification

balance = 5000

def deposite():
    global balance
    balance = balance + 1000
    
deposite()
print(balance)

#Exercise 3 — Nested Function + Enclosing Scope

def student():
    name = "Hardik"
    college = "Khyati College"

    def details():
        print(name)
        print(college)
        pass

    details()
student()


#Exercise 4 — nonlocal Counter

def counter():
    count = 0

    def increase():
        nonlocal count
        count += 1

    increase()
    increase()
    increase()
    print(count)

counter()


#Exercise 5 — Scope Bug Fix
total = 100

def add_amount():
    global total
    total = total + 50

add_amount()

print(total)


#Exercise 6 — LEGB + Shadowing

x = 10

def outer():
    x = 20

    def inner():
        x = 30
        print(x)   #---local
    inner()
    print(x)   #----enclosing
outer()
print(x)  #----global


#Exercise 7 — nonlocal + Global

score = 10

def outer():
    score = 20

    def inner():
        nonlocal score
        score += 10
    inner()
    print(score)
outer()
print(score)


#Exercise 8 — Realistic Scope Problem

def bank_account():
    balance = 5000

    def deposit():
        nonlocal balance
        balance += 1000
        
    def withdraw():
        nonlocal balance
        balance -= 500
            
    deposit()
    withdraw()
    print(balance)

bank_account()
"""

"""#Exercise 1 — Student Information

college = "Khyati College"

def student_info():
    name = "Hardik"
    age = 24
    print(name)
    print(age)
    print(college)
student_info()


#Exercise 2 — Global Counter

count = 0
def increase():
    
    global count
    count += 1
increase()
increase()
increase()
print(count)


#Exercise 3 — Local Variable Shadowing

name = "Hardik"

def show_name():
    name = "Rahul"
    print(name)
show_name()
print(name)


#Exercise 4 — Enclosing Scope

def company():
    company_name = "ABC Technologies"

    def show_company():
        print(company_name)
    show_company()
company()


#Exercise 5 — Fix the Scope Error
total = 100

def add():
    global total
    total = total + 50
    print(total)

add()


#Exercise 6 — nonlocal Counter

def counter():
    count = 0

    def increase():
        nonlocal count
        count += 1
    increase()
    increase()
    increase()
    increase()
    print(count)
counter()


#Exercise 7 — LEGB Challenge

x = 10

def outer():
    x = 20

    def inner():
        x = 30
        print(x)   #-----Local
    inner()
    print(x)   #----Enclosing
outer()
print(x)   #-----Global


#Exercise 8 — Real Scope Challenge

balance = 1000

def account():
    balance = 5000

    def deposit():
        nonlocal balance
        balance += 1000

    def withdraw():
        nonlocal balance
        balance -= 500
    
    deposit()
    withdraw()
    print(balance)

account()
print(balance)"""


                                        #Mini Project — Bank Account Manager

def bank_account():
    balance = 5000

    def deposit():
        deposit_amount = int(input("Enter Deposit Amount: "))
        nonlocal balance
        balance += deposit_amount

    def withdraw():
        withdraw_amount = int(input("Enter Withdraw Amount: "))
        nonlocal balance
        if withdraw_amount > balance:
            print("Insufficient Balance")
        else:
            balance -= withdraw_amount
        
    def show_balance():
        print(f"Current Balance: {balance}")
        
    
    while True:
        print("======= BANK ACCOUNT =======")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Show Balance")
        print("4. Exit")
        

        choice = input("Enter Your Choice: ")

        if choice == "1":
            deposit()

        elif choice == "2":
            withdraw()

        elif choice == "3":
            show_balance()

        elif choice == "4":
            print("Thank You For Using...")
            break
        else:
            print("Invalid Choice!!")
            
bank_account()
