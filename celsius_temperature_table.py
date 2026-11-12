#Daniel E Salazar Gomez
#CMP-131-86520
#Week 9 
#Lab 01
#Assigment 9
#11/12/2026
def fahrenheitToCelsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius 
def main():
    print("Fahrenheit to Celsius Converter")

    for Fahrenheit in range(21):
        celsius = fahrenheitToCelsius(fahrenheit)
        print(fahrenheit, "degrees F =", round(celsius, 2), "degrees C")
main()

