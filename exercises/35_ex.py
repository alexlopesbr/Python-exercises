# Write a program to approve the bank loan for a home purchase. Ask the value of the house, the buyer's salary and in how many years he will pay. The monthly payment cannot exceed 30% of the salary or the loan will be denied.

house_value = float(input('Enter the value of the house: '))
salary = float(input('Enter the buyer\'s salary: '))
years = int(input('Financing time in years: '))

monthly_payment = house_value / (years * 12)

if monthly_payment > salary * 0.3:
    print('Financing denied.')
else:
    print('Financing approved.')
