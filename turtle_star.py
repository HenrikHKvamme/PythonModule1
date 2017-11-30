import turtle

sideLength = int(input("How long do you want the sides to be?"))

myTurtle = turtle.Turtle()

side = 5

while side > 0:
    myTurtle.right(144)
    myTurtle.forward(sideLength)
    side = side - 1
turtle.done()
