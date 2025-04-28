import random
import sys
i = int(0)
x = random.randint(1, 100)

def win():
    print("You WON!!")
    sys.exit()


print("Guess the number between 1-100")
for i in range (0, 5):
    y = int(input("Guess the number"))
    if x > y:
        print("The number is higher")
    if x < y:
        print("The number is lower")
    if x == y:
        win()
    i += 1

print("You LOST!!!")