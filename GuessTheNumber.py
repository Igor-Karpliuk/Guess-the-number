import random
secretNumber = random.randint(1,20)
print("I am thinking of a number between 1 and 20, guess it")
for guessesTaken in range(1,7):
    print("take a guess")
    guess=int(input())

    if guess<secretNumber:
        print("your number is too low")
    elif guess>secretNumber:
        print("your number is too high")
    else:
        break

if guess == secretNumber:
    print("well done, faggot")
else:
    print(" you are wrong, i was thinking of " + str(secretNumber))
