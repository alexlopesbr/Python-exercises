# Write a program that converts a temperature by typing in degrees Celsius and converts it to degrees Fahrenheit.

temperature = float(input('Enter the temperature in Celsius: '))
celsius_to_fahrenheit = (temperature * 1.8) + 32

print('The temperature in Fahrenheit is: {}'.format(celsius_to_fahrenheit))
