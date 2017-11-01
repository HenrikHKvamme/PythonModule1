myConstPi = 3.14


#here we wnt to take an input from the user
print("Please enter the radius of the circle:")
radius = float(input())
print("You have entered a radius of", radius)

if(radius < 0):
    print("Radius f the crcle cannot be a negatve number")
print("The circumferance of the circle is:", 2*myConstPi*radius)
