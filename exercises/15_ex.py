# Create a program that reads any real number from the keyboard and displays its entire portion on the screen.
from math import trunc

number = float(input("Enter a real number: "))
print("The decimal part of the number is: {}" .format(trunc(number)))  # way 1
print("The decimal part of the number is: {}" .format(int(number)))  # way 2
