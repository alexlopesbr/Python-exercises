# The same teacher in challenge 19 wants to draw the order of presentation of students from students. Make a program that reads the names of the four students and shows the order

import random

students = []
count = 0

while (count < 4):
    students.append(
        input('Enter the name of the student: {}: '.format(count + 1)))
    count += 1

random_ordem = random.shuffle(students)

print('The students will be presented in the following order: {}'.format(students))
