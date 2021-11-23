# Develop a program that asks the distance of a trip in Km. Calculate the ticket price, charging R$0.50 per Km for trips of up to 200Km and R$0.45 for longer trips.

distance = float(input('Enter the distance of the trip: '))

if distance <= 200:
    price = distance * 0.50
else:
    price = distance * 0.45

print('The price of the trip is R${:.2f}'.format(price))
