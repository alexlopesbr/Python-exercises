# Make a program that reads a sentence from the keyboard and shows how many times the letter “A” appears, in which position it appears the first time, and in which position it appears the last time.

sentence = str(input('Enter a sentence: ')).upper()

print('The sentence has? {}, letter A.'. format(sentence.count('A')))
print('The first letter A appears in position {}'.format(sentence.find('A')+1))
print('The last letter A appears in position {}'.format(sentence.rfind('A')+1))
