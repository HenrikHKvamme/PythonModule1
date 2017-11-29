

def celciusToFahrenheit():
    myInput = int(input("Enter a temperature in Celcius: "))
    tempInFahrenheit = (myInput * 9 + 160) / 5
    print("The temperature of ", myInput, "in Celcius is ", tempInFahrenheit, "in Fahrenheit.")

def fahrenheitToCelcius():
    myInput = int(input("Enter a temperature in Fahrenheit: "))
    tempInCelcius = ((myInput-32)/9)*5
    print("The temperature of ", myInput, "in Fahrenheit is", tempInCelcius, "in Celcius.")
