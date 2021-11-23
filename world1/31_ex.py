# Make a program that reads any year and shows if it is a leap year.

year = int(input('Type a year: '))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('{} is a leap year.'.format(year))
else:
    print('{} is not a leap year.'.format(year))
