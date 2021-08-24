# Python Exercise 22: Create a program that reads a person's full name and displays:
# - The name in all upper and lower case letters.
# - How many letters in total (not including spaces).
# - How many letters has the first name. 

name = input('Enter your full name: ')
upper = name.upper()
lower = name.lower()
length = len(name) - name.count(' ')
first_name_len = len(name.split(' ')[0])

print(name, upper, length, lower, first_name_len)
