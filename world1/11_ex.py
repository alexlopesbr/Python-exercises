# Make an algorithm that reads the price of a product and shows its new price, with 5% off.

price = float(input('Enter the price of the product: '))

new_price = price - (price * 0.05)

print('The price with discount is {}'.format(new_price))
