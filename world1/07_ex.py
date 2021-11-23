# Write a program that reads a value in meters and displays it converted to centimeters and millimeters

value = float(input('Type a value in meters: '))

print('{0:.2f} km'.format(value / 1000))
print('{0:.2f} cm'.format(value * 100))
print('{0:.2f} mm'.format(value * 1000))
