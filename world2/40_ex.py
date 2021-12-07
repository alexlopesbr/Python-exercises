"""
The National Swimming Confederation needs a program that reads an athlete's year of birth and shows their category, according to age:
– Up to 9 years old: MIRIM

– Up to 14 years old: CHILDREN

– Up to 19 years old: JUNIOR

– Up to 25 years old: SENIOR

– Over 25 years old: MASTER
"""

athetes_age = int(input('Enter your age: '))

if athetes_age <= 9:
    print('MIRIM')
elif athetes_age <= 14:
    print('CHILDREN')
elif athetes_age <= 19:
    print('JUNIOR')
elif athetes_age <= 25:
    print('SENIOR')
else:
    print('MASTER')
