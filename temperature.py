import turtle
def celciusToFahrenheit():
    myInput = float(input("Enter a temperature in Celcius: "))
    tempInFahrenheit = (myInput * 9 + 160) / 5
    print("The temperature of ", myInput, "in Celcius is ", tempInFahrenheit, "in Fahrenheit.")
    myTurtle = turtle.Turtle()
    sides = 4
    while sides > 0:
        myTurtle.forward(tempInFahrenheit)
        myTurtle.left(90)
        sides = sides - 1
    turtle.done()


def fahrenheitToCelcius():
    myInput = float(input("Enter a temperature in Fahrenheit: "))
    tempInCelcius = ((myInput-32)/9)*5
    print("The temperature of ", myInput, "in Fahrenheit is", tempInCelcius, "in Celcius.")
    myTurtle = turtle.Turtle()
    sides = 4
    while sides > 0:
        myTurtle.forward(tempInCelcius)
        myTurtle.left(90)
        sides = sides -1
    turtle.done()
