import random

r = random.randrange(11)

n = input("Please choose a number between 1 and 10 ")

if int(n) == r:
    print("Good job!")
else:
    print("Wrong! The number was " + str(r) + ", please try again!")
