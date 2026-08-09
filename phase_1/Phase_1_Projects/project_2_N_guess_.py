                        #============================================
                                #PROJECT-2 NUMBER GUESSING GAME
                        #============================================

import random

random_number =random.randint(1,100)
guess_number = ""

count = 0
while guess_number != random_number:
        guess_number = int(input('Guess a Number between 1 to 100 :'))
        count += 1
        if guess_number > random_number:
                print("Too high")

        elif guess_number < random_number:
            print("Too low")

        else:
            print("Congrats You Win!!!!!!")

print("Attempt =", count)
