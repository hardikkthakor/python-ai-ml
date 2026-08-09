                            #=======================================
                                            #NESTED LOOP 
                            #=======================================
# #1
# for i in range(2):
#     print("Hello")

#     for j in range(2):
#         print("Hello")
    
# #2
# for i in range(2):
#     print("Rount",i)

#     for j in range(2):
#         print("Step")

# #3
# for i in range(3):
#     print("Start")

#     for j in range(2):
#         print(j)
#     print("End")

# #4
# for i in range(3):

#     for j in range(2):
#         print(i ,j)

# #5
# for i in range(2):
#     print("Python")

#     for j in range(2):
#         print("AI")
#     print("Done")


#                             #PRINTING STAR USING NESTED

# #1
# for i in range(4):
#     for j in range(i + 1):
#         print("*", end=" ")
#     print()

# #2
# for i in range(1,5):
#     for j in range(i):
#         print(i, end=" ")
#     print()

# #3
# for i in range(5):
#     for j in range(5 - i):
#         print("*", end= " ")
#     print()

# #4
# for i in range(5):
#     for j in range(5 - i):
#         print(j, end=" ")
#     print()

# #5
# for i in range(4):
#     for j in range(i):
#         print("*", end= " ")
#     print()

#6
for i in range(5):
    for j in range(i + 1):
        print("*", end=" ")
    print()

#7
for i in range(1,6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

#8
letters = ["A", "B", "C", "D", "E"]

for i in range(6):
    for j in range(i):
        print(letters[j], end=" ")
    print()

#9
for i in range(5):
    for j in range(5 - i):
        print("*", end= " ")
    print()

#10
for i in range(5,0,-1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

#11
for i in range(1,6):
    for j in range(i):
        print(i, end=" ")
    print()

#12
for i in range(1,6):
    for j in range(5,i - 1, -1):
        print(j, end=" ")
    print()

#13
for i in range(4,0,-1):
    for j in range(i,0,-1):
        print(j, end=" ")
    print()

#14
for i in range(1,6):
    for j in range(i,0,-1):
        print(j, end=" ")
    print()

#15
letters = ["A", "B", "C", "D", "E"]

for i in range(5):
    for j in range(i + 1):
        print(letters[i], end=" ")
    print()

#16

for i in range(1,6):
    for j in range(i):
        print("#", end=" ")
    print()

for i in range(4,0,-1):
    for j in range(i):
        print("#", end=" ")
    print()
