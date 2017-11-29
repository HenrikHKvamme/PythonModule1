import temperature


whatTemp = int(input("Type 1 for Celcius to Fahrenheit, or 2 for Fahrenheit to Celcius: "))
if whatTemp == 1:
    temperature.celciusToFahrenheit()

elif whatTemp == 2:
    temperature.fahrenheitToCelcius()
