# Sebastian Raschka 04/10/2014

import sys

def give_letter(word):
    for letter in word:
        yield letter

if sys.version_info[0] == 3:
    print('executed in Python 3.x')
    test = give_letter('Hello')
    print(next(test))
    print('in for-loop:')
    for l in test:
        print(l)

# if Python 2.x
if sys.version_info[0] == 2:
    print('executed in Python 2.x')
    test = give_letter('Hello')
    print(test.next())
    print('in for-loop:') 
    for l in test:
        print(l)
