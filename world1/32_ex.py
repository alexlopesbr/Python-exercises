# Make a program that reads three numbers and shows which is the largest and which is the smallest.

number_list = []

number1 = number_list.append(int(input('Enter the number 1: ')))
number2 = number_list.append(int(input('Enter the number 2: ')))
number3 = number_list.append(int(input('Enter the number 3: ')))

print('The largest number is {} and the smallest number is {}'.format(
    max(number_list), min(number_list)))
