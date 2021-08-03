# Write a program that asks how many kilometers a rental car has traveled and how many days it has been rented. Calculate the price to pay, knowing that the car costs R$60 per day and R$0.15 per km driven.

days_rented = int(input("How many days have you been with the car? "))
kilometers_driven = float(input("How many kilometers have you driven? "))
price_day = 60
price_km = 0.15
total = (days_rented * price_day) + (kilometers_driven * price_km)
print('The total is R${:.2f}' .format(total))
