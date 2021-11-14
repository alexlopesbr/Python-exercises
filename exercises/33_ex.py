# Write a program that asks for an employee's salary and calculates the amount of his raise. For salaries above R$1250.00, calculate a 10% increase. For inferiors or equals, the increase is 15%.

salary = float(input('Enter the employee\'s salary: '))

if salary >= 1250:
    salary_raise = salary * 0.10
else:
    salary_raise = salary * 0.15

print('The employee\'s raise is R${:.2f} and his new salary is {}.'.format(
    salary_raise, salary + salary_raise))
