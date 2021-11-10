# Make a program that reads any Integer and displays your times tables on the screen.

number = int(input('Enter a number: '))
count = 0
while count <= 10:
    print('{} X {:2} = {}'.format(number, count, number * count))
    count += 1