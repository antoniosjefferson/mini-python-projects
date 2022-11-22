import random

# TESTING RANDOM RANGE METHOD
# r = random.randrange(11)

# n = input("Please choose a number between 1 and 10 ")

# if int(n) == r:
#     print("Good job!")
# else:
#     print("Wrong! The number was " + str(r) + ", please try again!")

top_range = input("Please type a number between 1 and 10: ")

if top_range.isdigit():
    top_range = int(top_range)

    if top_range <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()

random_number = random.randrange(0, top_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue

    if user_guess == random_number:
        print("You got it in " + str(guesses) + " tries!")
        break
    elif user_guess > random_number:
        print("Too high!")
    else:
        print("Too low!")
