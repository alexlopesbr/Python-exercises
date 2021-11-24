# Create a program that reads two grades from a student and calculates their average, showing a message at the end, according to the average achieved: < 5 == disaproved, 5 - 6.9 == recovery, >= 7 == approved.

first_grade = float(input('Enter your first grade: '))
second_grade = float(input('Enter your second grade: '))

average = (first_grade + second_grade) / 2
average = round(average, 1)

if average >= 0 and average < 5:
    print('Your average is {}, you are Disapproved.'.format(average))
elif average >= 5 and average < 6.9:
    print('Your average is {}, you are Recovery.'.format(average))
elif average >= 7 and average <= 10:
    print('Your average is {}, you are Approved.'.format(average))
else:
    print('Invalid grade.')
