
#1

"""student = {
    "name": "Hardik",
    "age": 24,
    "country": "Germany"
}

print(student["name"])
print(student["age"])
print(student["country"])

student["country"] = "Canada"

student["dream"] = "AI Engineer"
student.pop("age")

if "age" in student:
    print("Found")
else:
    print("Not Found")"""

#2
"""company = {
    "CEO": "Sam Altman",
    "Company": "OpenAI",
    "Country": "USA"
}

for key in company:
    print(key)

for key in company:
    print(company[key])

for key, value, in company.items():
    print(key,":", value)"""

#3
"""marks = {
    "Math": 85,
    "Science": 92,
    "English": 78
}

print(marks["Math"])
print(marks["Science"])
print(marks["English"])

marks["English"] = 90

for key, value, in marks.items():
    print(key, "=", value)"""

#4
"""person = {
    "name": "Hardik",
    "age": 24,
    "city": "Ahmedabad"
}

print(person)

person["city"] = "Berlin"
person["dream"] = "AI Engineer"

person.pop("age")

if "age" in person:
    print("Exist")
else:
    print("Not Exist")

for key, value, in person.items():
    print(key, ":", value)"""