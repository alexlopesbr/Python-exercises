# Develop a program that reads the length of three lines and tells the user whether or not they can form a triangle.

line1 = float(input('Enter the length of the first line: '))
line2 = float(input('Enter the length of the second line: '))
line3 = float(input('Enter the length of the third line: '))

if line1 + line2 > line3 and line1 + line3 > line2 and line2 + line3 > line1:
    print('Yes, you can form a triangle.')
else:
    print('No, you cant form a triangle.')
