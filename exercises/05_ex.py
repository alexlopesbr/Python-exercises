# Create an algorithm that reads a number and shows its double, triple and square root.

number = int(input('Enter a number: '))

double = number * 2
triple = number * 3
squere_root = number ** 0.5

print('Double of {} is {}'.format(number, double))
print('Triple of {} is {}'.format(number, triple))
print('Square root of {} is {:.2f5}'.format(number, squere_root))
