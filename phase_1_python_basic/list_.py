"""countries = ["India", "Germany","UK","US","UAE"]
print(countries)"""


"""fav_num = [10,20,30,40,50]
print(fav_num)
"""
"""data = ["Hardik", 24,"Germany",True]
print(data)"""

"""# cities = ["Berlin", "Tokyo", "Delhi", "London"]
# print(cities[1])"""

"""marks = [80, 90, 75, 95]
print(marks[3])"""

"""names = ["Hardik", "Rahul", "Priya", "Aman"]
print(names[0])
print(names[2])"""


#7

"""countries = ["India", "Germany", "Japan", "Canada"]

print(countries[0])
print(countries[3])"""

# #8

"""numbers = [5,10,15,20,25]

print(numbers[1])
print(numbers[3])
print(numbers[4])"""

# #9
"""friends = ["Rahul", "Aman", "Priya", "Hardik"]

print(friends[1])
print(friends[3])"""

# #10
"""languages = ["Python", "Java", "C++", "JavaScript", "Go"]

print(languages[-1])
print(languages[-2])
print(languages[-5])"""

# #11 
"""countries = ["India","Germany","Japan"]

countries[1] = "Canada"
print(countries)"""

# #12
"""marks = [70,80,90]
marks[0] = 95
print(marks)"""

# #13
"""friends = ["Rahul", "Aman","Priya"]
friends[2] = "Hardik"
print(friends)"""

# #14
"""numbers = [5,10,15,20]
numbers[0]= 50
numbers[-1] = 200
print(numbers)"""


                                    #================
                                        #append()
                                    #================
# #15
"""fruits = ["Apple", "Banana"]
fruits.append("Mango")
print(fruits)"""

# #16
"""marks = [80, 90]
marks.append(100)
print(marks)"""

# #17
"""friends = []
friends.append("Hardik")
friends.append("Rahul")
friends.append("Priya")
print(friends)"""

                                    #================
                                    #insert(index,value)
                                    #================
#18
"""name = ["Rahul", "Priya"]
name.insert(0,"Hardik")
print(name)"""

# #19
"""marks = [80,100]
marks.insert(1,90)
print(marks)"""

# #20
"""color = ["Red", "Green"]
color.insert(1, "Blue")
print(color)"""

# #21
"""number = [10,30,40]
number.insert(1,20)
print(number)"""

                                    #================
                                        #remove(value)
                                    #================
#22
"""countries = ["India", "Germany", "Japan"]
countries.remove("Japan")
print(countries)"""

# #23
"""marks = [70, 80, 90, 100]
marks.remove(90)
print(marks)"""

# #24
"""friends = ["Hardik", "Rahul", "Priya"]
friends.remove("Rahul")
print(friends)"""

# #25
"""numbers = [10, 20, 30, 40, 50]
numbers.remove(20)
numbers.remove(40)
print(numbers)"""

                                    #================
                                        #pop(index)
                                    #================

# #26
"""countries = ["India", "Germany", "Japan"]
countries.pop(1)
print(countries)"""

# #27
"""marks = [70, 80, 90, 100]
marks.pop()
print(marks)"""

# #28
"""friends = ["Hardik", "Rahul", "Priya"]
friends.pop(0)
print(friends)"""

# #29
"""numbers = [10, 20, 30, 40, 50]
numbers.pop() #if we dont write index number then it will remove last value automatically
print(numbers)"""

                                    #================
                                        #sort()
                                    #================
#30
"""numbers = [25, 5, 15, 10]
numbers.sort()
print(numbers)"""

# #31
"""marks = [85, 60, 95, 70]
marks.sort(reverse=True)
print(marks)"""

# #32
"""friends = ["Rahul", "Hardik", "Aman", "Priya"]
friends.sort()
print(friends)"""

# #33
"""countries = ["Japan", "Germany", "India", "Canada"]
print(countries)

countries.sort()
print(countries)

countries.sort(reverse= True)
print(countries)"""

                                    #================
                                        #reverse()
                                    #================
#34
"""fruits = ["Apple", "Banana", "Mango"]
fruits.reverse()
print(fruits)"""

# #35
"""marks = [60, 70, 80, 90]
marks.reverse()
print(marks)"""

# #36
"""friends = ["Hardik", "Rahul", "Priya", "Aman"]
friends.reverse()
print(friends)"""

# #37
"""numbers = [25, 5, 15, 10]
print(numbers)

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)"""

                                    #================
                                        #len()
                                    #================
#38
"""fruits = ["Apple", "Banana", "Mango", "Orange"]
print(len(fruits))"""

# #39
"""marks = [80, 90, 95]
print(len(marks))
"""
# #40
"""friends = ["Hardik", "Rahul", "Priya", "Aman", "Neha"]
print(len(friends))"""

# #41
"""numbers = [10, 20, 30]
print(numbers)
print(len(numbers))

numbers.append(40)
print(len(numbers))"""


                        #============================
                                #LIST + FOR
                        #============================

# #42
"""fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)"""

# #43
"""marks = [80, 90, 95, 70]

for mark in marks:
    print(mark)"""

# #44
"""friends = ["Hardik", "Rahul", "Priya"]

for fri in friends:
    print("Welcome",fri)"""


                        #============================
                        #SUM USING FOR LOOP (ACCUMULATOR)
                        #============================
#45
"""numbers = [10, 20, 30, 40, 50]
total = 0

for num in numbers:
    total = total + num
print(total)"""

# #46
"""marks = [80, 90, 95]
total = 0

for i in marks:
    total = total + i
print(total)"""

# #47
"""prices = [150, 200, 50, 100]
total = 0

for i in prices:
    total = total + i
print(total)"""


                        #============================
                        #FIND THE LARGEST NUM USING LIST AND LOOP
                        #============================

#48
"""marks = [80,90,95,70]

largest = marks[0]

for mark in marks:
    if mark > largest:
        largest = mark
print(largest)"""

#49
"""prices = [150,200,50,100]

highest = prices[0]

for price in prices:
    if price > highest:
        highest = price
print(highest)"""

#50
"""ages = [24, 18, 30, 27, 21]

old_age = ages[0]

for age in ages:
    if age > old_age:
        old_age = age
print(old_age)"""



                                #SMALEST NUMBER 

# #51
"""marks = [80, 90, 95, 70]

smallest = marks[0]

for mark in marks:
    if mark < smallest:
        smallest = mark
print(smallest)"""

# #52
"""prices = [150, 200, 50, 100]

lowest = prices[0]

for price in prices:
    if price < lowest:
        lowest = price
print(lowest)"""

# #53
"""ages = [24, 18, 30, 27, 21]

y_age = ages[0]

for age in ages:
    if age < y_age:
        y_age = age
print(y_age)"""


                            #=======================================
                                    #Counting Using a Loop
                            #=======================================
#54   --EVEN NUMBER--

"""numbers = [10, 25, 40, 55, 60]
count = 0

for num in numbers:
    if num % 2 ==0:
        count += 1
print(count)"""

#55
"""numbers = [11, 20, 33, 44, 55]
count = 0

for num in numbers:
    if num % 2 != 0:
        count += 1
print(count)
"""
#56
"""ages = [15, 18, 22, 14, 30, 17]
count = 0

for age in ages:
    if age >=18:
        count += 1
print(count)"""

                            #=======================================
                                    #SEARCHING IN LIST
                            #=======================================
#57
"""friends = ["Hardik", "Rahul", "Priya"]

if "Rahul" in friends:
    print("Found")
else:
    print("Not Found")"""

#58
"""countries = ["India", "Germany", "Japan"]

if "Canada" in countries:
    print("Found")
else:
    print("Not Found")"""

#59
"""numbers = [10, 20, 30, 40]

if 30 in numbers:
    print("Found")
else:
    print("Not Found")"""

                            #=======================================
                                    #SEARCHING IN LIST  by --> NOT IN
                            #=======================================
#60
"""friends = ["Hardik", "Rahul", "Priya"]

if "Aman" not in friends:
    print("New Friend")
else:
    print("Old Friend")"""

#61
"""countries = ["India", "Germany", "Japan"]

if "Germany" not in countries:
    print("Not Found")
else:
    print("Found")"""

#62
numbers = [10, 20, 30, 40]

if 50 not in numbers:
    print("Not Exist")
else:
    print("Exist")

