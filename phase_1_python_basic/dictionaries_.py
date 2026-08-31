
#1

"""info = {
    "name": "Hardik",
    "dream": "AI Engineer",
    "country": "Germany",
}

print(info)
print(info["name"])
print(info["dream"])
print(info["country"])"""


#2

"""car = {
    "brand": "BMW",
    "color": "Black"
}

car["year"] = 2025
car["color"] = "White"

car.pop("brand")

if "year" in car:
    print("Exist")
else:
    print("Not Exist")

print(car)"""


#3
student = {
    "name": "Hardik",
    "dream": "AI engineer",
    "country": "Germany"
}

for key in student:
    print(key)

for key in student:
    print(student[key])

for key, value in student.items():
    print(key,":", value)


#4
car = {
    "brand": "BMW",
    "color": "Black",
    "year": 2025
}

for key, value in car.items():
    print(key, ":", value)