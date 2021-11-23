# Make a program that reads a person's full name, then displays the first and last name separately.

full_name = str(input('Enter your full name: ')).split(' ')
print('Your first name is {}, and your last name is {}'. format(
    full_name[0], full_name[-1]))
