# A teacher wants to draw one of his four students to erase the board. Make a program that helps him by reading the names of the students and writing the name of the chosen one on the screen.
import random

students = []
count = 0

while (count < 4):
    students.append(
        input('Enter the name of the student: {}: '.format(count + 1)))
    count += 1

student_selected = random.choice(students)
print('The student selected is {}'.format(student_selected))
