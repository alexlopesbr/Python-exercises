# Make a program that reads something from the keyboard and displays its primitive type and all possible information about it on the screen.

something = input("Enter something: ")

print('Type: ', type(something).__name__)
print('Have space? : ', something.isspace())
print('Is alphanumeric? : ', something.isalnum())
print('Is numeric? : ', something.isnumeric())
print('Is alpha? : ', something.isalpha())
print('Is lowercase? : ', something.islower())
print('Is uppercase? : ', something.isupper())
print('Is titlecase? : ', something.istitle())
print('Is capitalized? : ', something.capitalize())
print('Length: ', something.__len__())
