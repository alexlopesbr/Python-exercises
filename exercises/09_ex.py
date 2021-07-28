# Create a program that reads how much money a person has in their wallet and shows how many dollars they can buy.

money = float(input("How much money do you have in your wallet? R$"))
quote = float(input("Type the dollar quote: US$"))
result = money / quote

print('you can buy US${:.2f} dollars'.format(result))

