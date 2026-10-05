


# Q1
# Create a class named Movie.
# Use __init__() to store title and year.
# Create one object and print both values.

"""
class Movie:
    
    def __init__(self, title,year):
        self.title = title
        self.year = year
movie1 = Movie("Mirzapur the movie",2026)
movie2 = Movie("HANUMAN ANSH",2026)

print(movie1.title,movie1.year)
print(movie2.title, movie2.year)


# Q2
# Create a class named Mobile.
# Use __init__() to store brand, model, and price.
# Create two objects and print each object's details.

class Mobile:

    def __init__(self,brand,model,price):
        
        self.brand = brand
        self.model = model
        self.price = price

mobile1 = Mobile("Apple","iPhone12",63000)
mobile2 = Mobile("One+","One+ Nord 6",25000)

print(mobile1.brand,mobile1.model,mobile1.price)
print(mobile2.brand,mobile2.model,mobile2.price)


# Q3
# Create a class named Student.
# Use __init__() to store name and marks.
# Create two objects and print their names and marks.

class Student:

    def __init__(self,name, marks):
        
        self.name = name
        self.marks = marks

student1 = Student("Hardik",99)
student2 = Student("Anjali",99)

print(student1.name,student1.marks)
print(student2.name,student2.marks)

#------------------------------------------------------------------------------
#Instance Variables vs Class Variables

# Q1
# Create a class named Product.
# Add a class variable: category = "Electronics".
# Use __init__() for name and price.
# Create two product objects and print their data.

class Product:
    category = "Electronics"

    def __init__(self, name, price):        

        self.name = name
        self.price = price

product1 = Product("ASUS Laptop",48000)
product2 = Product("iPhone12", 630000)

print(product1.name,product1.price)
print(product2.name,product2.price)


# Q2
# Create a class named Student.
# Add a class variable: school = "ABC School".
# Use __init__() for name and marks.
# Create two students and print their own data plus the shared school.

class Student:
    school = "ABC School"

    def __init__(self, name, marks):

        self.name = name
        self.marks = marks

student1 = Student("Hardik",99)
student2 = Student("Anjali", 99)

print(student1.name,student1.marks,student1.school)
print(student2.name,student2.marks,student2.school)


# Q3
# Create a class named Employee.
# Add a class variable: company = "Google".
# Use __init__() for name and job_role.
# Create one employee and print all three values.

class Employee:
    company = "Google"

    def __init__(self, name, job_role):

        self.name = name
        self.job_role = job_role

employee1 = Employee("Hardik","Software Engineer")
employee2 = Employee("Anjali","AI/ML Engineer")

print(employee1.name,employee1.job_role,employee1.company)
print(employee2.name,employee2.job_role,employee2.company)


#----------------------------------------------------------------
#Methods

# Q1
# Create a class named Greeting.
# Add a method say_hello() that prints:
# "Hello, Python!"
# Create an object and call the method.

class Greeting:

    def say_hello(self):
        print(f"Hello, Python!")

greeting = Greeting()
greeting.say_hello()


# Q2
# Create a class named Rectangle.
# Use __init__() for length and width.
# Add a method area() that returns length × width.
# Create an object and print its area.

class Ractangle:

    def __init__(self, length, width):

        self.length = length
        self.width = width
    
    def area(self):
        
        return self.length * self.width
    
ractangle_area = Ractangle(5,10)
print(f"The Are of the ranctange is: {ractangle_area.area()}")


# Q3
# Create a class named BankAccount.
# Use __init__() for account_holder and balance.
# Add a method show_balance() that prints the holder's name and balance.
# Create an object and call the method.

class BankAccount:

    def __init__(self, account_holder, balance):

        self.account_holder = account_holder
        self.balance = balance

    def show_balance(self):
        print(f"{self.account_holder} : {self.balance}")

    
    def deposite(self,amount):
        if amount > 0:
            self.balance += amount
            print(f"Successfully Deposit Amount: {amount}")
            print(f"Updated Balance: {self.balance}")
        else:
            print("Deposit Amount Must be greater then 0")


ac_holder1 = BankAccount("Hardik", 500000)
ac_holder2 = BankAccount("Anjali", 850000)
ac_holder1.deposite(150000)

ac_holder1.show_balance()
ac_holder2.show_balance()

# Q4
# Add a deposit(amount) method to BankAccount.
# It should add amount to balance and print the updated balance.

#------------------------------------------------------------------------
#6. Inheritance
"""
# Q1
# Create a parent class Vehicle with a method start().
# It should print: "Vehicle started".
#
# Create a child class Car that inherits Vehicle.
# Create a Car object and call start().

class Vehicle():

    def start(self):
        print("Vehicle Started..")

class Car(Vehicle):
    pass

car_start = Car()
car_start.start()


# Q2
# Create a parent class Person.
# Its __init__() should store name.
#
# Create a child class Employee.
# Its __init__() should store name and job_role.
# Use super().__init__(name).
#
# Create an Employee object and print name and job_role.

class Person:

    def __init__(self, name):
        self.name = name

class Employee(Person):

    def __init__(self,name, job_role):
        super().__init__(name)
        self.job_role = job_role


emp = Employee("Hardik","Software Engineer")
print(emp.name,emp.job_role)


# Q3
# Create a parent class Animal with a method eat().
#
# Create child classes Dog and Cat.
# Dog should have bark().
# Cat should have meow().
#
# Create one object of each child class.
# Call eat() plus the child-specific method for both objects.

class Animal:

    def eat(self):
        print("The animal is eating..")

class Dog(Animal):

    def bark(self):
        print("Dog is Barking")

class Cat(Animal):

    def meow(self):
        print("The cat says..Meow Meow")

my_dog = Dog()
my_cat = Cat()

my_dog.eat()
my_dog.bark()

my_cat.meow()


# Q4
# Create a parent class Account with __init__(owner, balance).
#
# Create a child class SavingsAccount with an extra interest_rate.
# Use super() to set owner and balance.
#
# Create an object and print owner, balance, and interest_rate.

class Account:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

class SavingsAccount(Account):

    def __init__(self, owner, balance,interest_rate):
        super().__init__(owner,balance)
        self.interest_rate = interest_rate

details = SavingsAccount("Hardik", 1000000,0.5)
print(details.owner,details.balance,details.interest_rate)


#------------------------------------------------------------------
#Polymorphism — practice

# Q1
# Create classes Circle and Square.
# Both must have an area() method.
#
# Circle area: 3.14 * radius * radius
# Square area: side * side
#
# Create objects and call area() for both.

class Circle:

    def __init__(self, radius):
        self.radius = radius


    def area(self):
        return 3.14 * self.radius * self.radius

class Square:

    def __init__(self, side):
        self.side = side

    
    def area(self):
        return self.side * self.side

Circle_area = Circle(5)
Square_area = Square(4)

print(Circle_area.area())
print(Square_area.area())


# Q2
# Create a parent class Notification with send().
#
# Create EmailNotification and SMSNotification child classes.
# Override send() in each child class with different messages.
#
# Store both objects in a list and call send() in a loop.

class Notification:

    def send(self):
        pass
        
class EmailNotification(Notification):

    def send(self):
        print("Email Notification...")
    
class SMSNotification(Notification):

    def send(self):
        print("SMS Notification...")


all_notification = [EmailNotification(),SMSNotification()]

for notification in all_notification:
    notification.send()


# Q3
# Create classes CreditCard and UPI.
# Both should have a pay(amount) method.
#
# CreditCard prints: "Paid <amount> using Credit Card"
# UPI prints: "Paid <amount> using UPI"
#
# Store both payment objects in a list and call pay(500) for each.

class CreditCard:

    def pay(self,amount):
        print(f"Paid {amount} using Credit Card")

class UPI:

    def pay(self,amount):
        print(f"Paid {amount} using UPI")

payments = [CreditCard(),UPI()]

for p in payments:
    p.pay(500)


#--------------------------------------------------------------
#Encapsulation — practice

# Q1
# Create a class named Student.
# Use __init__() for name and __marks.
#
# Add:
# - get_marks() → returns marks
# - update_marks(new_marks) → updates marks only if 0 <= new_marks <= 100
#
# Create an object, update marks, and print final marks.

class Student:

    def __init__(self,name,marks):
        self.name = name 
        self.__marks = marks

    
    def get_marks(self):
        return self.__marks
    
    def update_marks(self,new_marks):

        if 0 <= new_marks <= 100:
            self.__marks = new_marks

s1 = Student("Hardik", 88)

print(f"Old Marks: {s1.name} : {s1.get_marks()}")

s1.update_marks(98)

print(f"Updated Marks: {s1.name} : {s1.get_marks()}")


# Q2
# Create a class named BankAccount.
# Use __init__() for account_holder and __balance.
#
# Add:
# - deposit(amount): adds only positive amounts
# - withdraw(amount): allows withdrawal only when:
#   amount > 0 and amount <= balance
# - get_balance(): returns balance
#
# Test deposit and withdrawal, then print final balance.

class BankAccount:

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance
    

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
    

    def get_balance(self):
        return self.__balance
    

my_account = BankAccount("Hardik", 4000.0)

my_account.deposit(5000)
my_account.withdraw(2000)

print(f"Final Balance Amount: {my_account.account_holder} : {my_account.get_balance()}")


# Q3
# Create a class named Product.
# Store __price as private-like data.
#
# Add:
# - get_price()
# - set_price(new_price): updates only if new_price > 0
#
# Create an object, try a valid price update, and print the final price.

class Product:

    def __init__(self,price):
        self.__price = price
    
    def get_price(self):
        return self.__price
    
    def set_price(self,new_price):
        if new_price > 0:
            self.__price = new_price
            
    
store = Product(500)
print(f"Old Price: {store.get_price()}")
store.set_price(780)
print(f"Updated Price: {store.get_price()}")


#---------------------------------------------------------
# Abstraction — practice

# Q1
# Import ABC and abstractmethod.
#
# Create an abstract class Animal.
# Add an abstract method sound().
#
# Create Dog and Cat child classes.
# Each must implement sound() with its own message.
#
# Create both objects and call sound().

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):

    def sound(self):
        print("Bark")
    
class Cat(Animal):

    def sound(self):
        print("Meow")

sounds = [Dog(), Cat()]

for s in sounds:
    s.sound()


# Q2
# Create an abstract class Shape.
# Add an abstract method area().
#
# Create Rectangle and Square child classes.
# Each must implement area() with its own formula.
#
# Create objects and print their areas.

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Rectange(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width
    
class Square(Shape):

    def __init__(self, side):
        self.side = side

    def area(self):
        
        return self.side * self.side
    
rectangle_area = Rectange(10, 5)
square_area = Square(4)

print(rectangle_area.area())
print(square_area.area())


# Q3
# Create an abstract class Login.
# Add an abstract method authenticate().
#
# Create GoogleLogin and EmailLogin child classes.
# Each prints a different successful-login message.
#
# Store both objects in a list and call authenticate() in a loop.


from abc import ABC, abstractmethod

class Login(ABC):

    @abstractmethod

    def authenticate(self):
        pass

class GoogleLogin(Login):

    def authenticate(self):
        print("Google Login Successful")

class EmailLogin(Login):

    def authenticate(self):
        print("Email Login Successful")

message = [GoogleLogin(), EmailLogin()]

for m in message:
    m.authenticate()

