# Make a program that reads a young person's year of birth and tells them, based on their age, whether they are still enlisting, whether it is an exact time to enlist, or whether enlistment time is past. Your program should also show you the time that is missing or past the deadline.

age_person = int(input('Enter your age: '))
enlistment_age = 18

if age_person < enlistment_age:
    print('You are still enlisting.')
    print('You have', enlistment_age - age_person, 'years to enlist.')
elif age_person == enlistment_age:
    print('You are enlisting now.')
else:
    print('You are past enlistment.')
    print('You have', age_person - enlistment_age, 'years past enlistment.')
