# Develop a program that reads a student's two grades, calculates and displays their average.

first_grade = float(input("Please enter your first grade: "))
second_grade = float(input("Please enter your second grade: "))
avarage = (first_grade + second_grade) / 2

print('Your avarage is: {:.1f}'.format(avarage))
