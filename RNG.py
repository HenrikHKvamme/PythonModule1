import random

minNumber = int(input("Minimum number: "))
maximumNumber = int(input("Maxmum number: "))
myRandomNumber = random.randint(minNumber, maximumNumber)
maxTries = 5

numberGuessed = int(input("Guess a number: "))

while numberGuessed < minNumber or numberGuessed > maximumNumber:
    numberGuessed = int(input("That number is not in range. Try again:"))

tries = 0

while(tries < maxTries):
    if numberGuessed != myRandomNumber:
        print("Incorrect, Try again! :")
        tries = tries + 1
        print("You have",5-tries,"remaining")
        numberGuessed = int(input("Guess again:"))
        while numberGuessed < minNumber or numberGuessed > maximumNumber:
            numberGuessed = int(input("That number is not in range. Try again:"))
    if numberGuessed == myRandomNumber:
        print("Correct!!! The number was", myRandomNumber)
        exit(0)

if tries == 5:
    print("You lose! The number was:", myRandomNumber)


# 1) What if we enter numbers outside the range
# 2) make a way to continue playing the game
