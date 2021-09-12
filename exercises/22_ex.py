# Write a program that reads a number from 0 to 9999 and displays each of the separate digits on the screen.

number = int(input("Enter a number from 0 to 9999: "))

thousand = number // 1000
hundred = (number % 1000) // 100
ten = (number % 100) // 10
one = number % 10

print("Thousand: {}\nHundred: {}\nTen: {}\nOne: {}".format(thousand, hundred, ten, one))