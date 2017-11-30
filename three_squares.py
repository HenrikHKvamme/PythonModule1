import turtle

myTurtle = turtle.Turtle()

side = 4


while side > 0:
    myTurtle.forward(400)
    myTurtle.right(90)
    side = side -1

myTurtle.right(45)
myTurtle.penup()
myTurtle.forward(100)
myTurtle.pendown()
myTurtle.left(45)

side = 4

while side > 0:
    myTurtle.forward(250)
    myTurtle.right(90)
    side = side - 1

myTurtle.right(45)
myTurtle.penup()
myTurtle.forward(65)
myTurtle.left(45)
myTurtle.pendown()

side = 4

while side > 0:
    myTurtle.forward(160)
    myTurtle.right(90)
    side = side - 1


turtle.done()
