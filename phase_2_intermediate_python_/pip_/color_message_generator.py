

                                        #PIP Mini Project — Terminal Color Message Generator

import random
from colorama import Fore,Style

name = input("Enter Your Name: ")

messages = [
        "Never Give-up",
        "Believe In YourSelf",
        "Focus On Your Goals",
        "Do Your Best There Is No Plan B",
        "You Can Do It"
    ]

selected = random.choice(messages)
print(Fore.BLUE + f"Hello {name}")
print(Fore.RED + f"Today's Motivation:\n{selected}")

print(Style.RESET_ALL)