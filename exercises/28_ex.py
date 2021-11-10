# Write a program that reads the speed of a car. If he goes over 80km/h, show a message saying he was fined. The fine will cost R$7.00 for each km over the limit.

speed_limit = 80
Your_speed = int(input('Enter your speed: '))


if Your_speed > speed_limit:
    fine_amount = (Your_speed - speed_limit) * 7   
    print('You were fined for going over the speed limit.')
    print('Your fine is R${}'.format(fine_amount))
else:
    print('You were not fined.')