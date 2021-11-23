# Make an algorithm that reads an employee's salary and shows their new salary, with a 15% increase.

salary = float(input('Enter the employee's salary: '))
increase = 15
new_salary = salary + (salary * increase / 100)

print('The new employee\'s salary with {}% increase: {}'.format(
    increase, new_salary))
