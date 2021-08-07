# Write a program that reads the length of the opposite side and the adjacent side of a right triangle. Calculate and show the length of the hypotenuse.
from math import hypot

opposite_leg = float(input("Enter the length of the opposite leg: "))
adjacent_leg = float(input("Enter the length of the adjacent leg: "))

hipotenuse = (opposite_leg**2 + adjacent_leg**2) ** 0.5
hipotenuse2 = hypot(opposite_leg, adjacent_leg)

print('The hipotenuse is: {:.2f}'.format(hipotenuse2))
