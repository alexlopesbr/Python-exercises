# Write a program that makes the computer “think” of an integer between 0 and 5 and ask the user to try to find out which number was chosen by the computer. The program should write on the screen if the user won or lost.
from random import randint

number = int(input("Guess a number between 0 and 5: "))

if number >= 0 and number <= 5:
    if number == randint(0, 5):
        print("You won!")
    else:
        print("You lost!")
else:
    print('Only numbers beetwing 0 and 5')
