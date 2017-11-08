currentYear = int(input("What year are we in now? "))
birthYear = int(input("Please enter the year in whitch you were born. "))

if birthYear > currentYear:
    print("You are not yet born.")
    exit(0)

if birthYear <= 1900:
    print("That is too old!")
    exit(0)

if (currentYear - birthYear) > 120:
    print("You can not be that old.")
    exit(0)
theYearIEntered = int(input("Please enter a year in the future. "))

if (theYearIEntered-birthYear) < 0:
    print("That is impossible!.")
    exit(0)

print("My age in", theYearIEntered, "Will be:", theYearIEntered - birthYear)
