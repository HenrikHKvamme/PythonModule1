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

if birthYear == currentYear:
    print("Congratulations on being born!!!")

if (currentYear - birthYear) == 100:
    print("Congratulations on 100 years!!!")

if  13 <= (currentYear - birthYear) <=19:
    print("Greeting teenager!")

decade = 10

while decade <= (currentYear - birthYear):
    if (currentYear - birthYear) == decade:
        print("Welcome to a new decade!!")
    decade = decade + 10

age = (currentYear - birthYear)

if age > 1:
    for i in range(2,age):
        if (age % i) == 0:
            print("Your age is not a prime number.")
            break
    else:
        print("Your age is a prime number!")

strAge = str(age)
added = 0

for ch in strAge:
    added = added + int(ch)

print("The numbers in your age added together is:",added)
print("Your age in", theYearIEntered, "Will be:", theYearIEntered - birthYear)



#Tasks for homework
# 1) What iff irs a new born baby? Greet him/her.
# 2) What if someone's age comes up as 100! congratulat him/her.
# 3) What if someone's age is between 13 and 19? Say hello to the teenager.
# 4) If the person is 10, 20, 30... invite them to a new decade
# 5) If the person's age is a prime number, tell them about it
# 6) Add up the digits in their birth year
