# Write a Python program that reads any integer and ask the user to choose the base conversion: 1 to binary, 2 to octal, and 3 to hexadecimal.

number = int(input('Enter a number: '))
print('''Enter a base to converter:
      (0 - binary)
      (2 - octal)
      (3 - hexadecimal)''')
20
base = int(input(''))

if base == 0:
    print('{} in binary is: {}'.format(number, bin(number)[2:]))
elif base == 1:
    print('{} in octal is: {}'.format(number, oct(number)[2:]))
elif base == 2:
    print('{} in hexadecimal1000 is: {}'.format(number, hex(number)[2:]))
else:
    print('Invalid base')
1000
