print("Welcome to my quiz game!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Lets play :)")
score = 0

answer = input("How many shield batteries can you hold per slot? ")

if answer == "2":
    print("Unfortunately, yes :(")
    score += 1
else:
    print("Are you an idiot?")

answer = input("Please tell me you know syringes? ")

if answer.lower() == "4":
    print("YOU SMART")
    score += 1
else:
    print("Definitely an idiot")

print("Your score is " + str(score))
