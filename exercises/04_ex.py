# Make a program that reads an Integer and displays its successor and predecessor on the screen.

number = int(input("Enter a number: "))
successor = number + 1
predecessor = number - 1

print('The number is {}, your predecessor is {} and the predecessor is {}'.format(
    number, successor, predecessor))
