


                            #=============================
                                        #STRING
                            #=============================
#1
country = "Germany"

print(country)
print(country[0])
print(country[-1])
print(len(country))

#2
dream = "AI Engineer"

print(dream[3])
print(dream[7])
print(dream[-1])
print(len(dream))


#3
dream = "ai engineer"

print(dream)
print(dream.upper())
print(dream.title())

#4
country = "GERMANY"

print(country)
print(country.lower())

#5 REPLACE()
sentence = "I want to become an Doctor"

print(sentence.replace("Doctor", "AI Engineer"))

#6
language = "Java is good"
print(language.replace("Java", "Python"))

#7   FIND()
sentence = "I want to become AI Engineer"
print(sentence.find("AI"))
print(sentence.find("Engineer"))

#8
city = "Ahmedabad"

print(city.find("m"))
print(city.find("d"))
print(city.find("z"))


#9 COUNT()
sentence = "I love Python because Python is awesome"
print(sentence.count("Python"))

#10
city = "Ahmedabad"
print(city.count("a"))
print(city.count("d"))
print(city.count("z"))


                                    #11  STARTWITH() ENDWITH()

website = "openai.com"

print(website.startswith("open"))
print(website.endswith(".com"))
print(website.endswith(".org"))                                    

#12
email = "hardik@gmail.com"

print(email.startswith("hardik"))
print(email.endswith(".com"))
print(email.startswith("Hardik"))

                                    #12 STRIP()

username = "    Buddy    "

print(username)
print(username.strip())

#13
country = "     Germany     "

country = country.strip()
print(country)


                                #13 SPLIT()
sentence = "Germany is my dream country"

print(sentence.split())

#14
skills = "Python,AI,Machine Learning"

print(skills.split(","))

                                    #15  JOIN()
dreams = ["Python", "AI", "Germany"]
print(" ".join(dreams))
print(" -> ".join(dreams))

#16
letters = ["B", "U", "D", "D", "Y"]
print("".join(letters))