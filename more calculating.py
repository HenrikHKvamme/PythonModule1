import random
inputName = False
while inputName == False:
    namePerson = input("Whats your name?")
    nameLen = int(len(namePerson))
    nameCheck = nameLen
    if nameLen < 1:
        print("empty")
    elif:
        while nameCheck > 0:

    else:
        inputName = True
        break

rng = random.randint(1, (nameLen + 3))

print(rng)



if nameLen > rng:
    print("Hooray!")
elif rng > nameLen:
    print("Nooooo!")
elif rng == nameLen:
    print("Equal")
