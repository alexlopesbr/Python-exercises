# Write a program that reads two whole numbers and compares them. showing on the screen a message:

number1 = int(input('Enter the number 1: '))
number2 = int(input('Enter the number 2: '))

if number1 > number2:
    print('{} is bigger than {}.'.format(number1, number2))
elif number1 < number2:
    print('{} is bigger than {}.'.format(number2, number1))
else:
    print('{} is equal to {}.'.format(number1, number2))
