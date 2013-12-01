# Examples for using Python's Regular expression module "re"
# sr 11/30/2013

import re

'''OVERVIEW
     '*' matches all characters that follow (0 or more)
     '+' matches all characters that follow (1 or more)
     '?' makes the previous character optional
     '{4}' previous character must match exactly 4 times
<<<<<<< HEAD
     '{2-4}' previous character must match exactly 2-4 times
     '[0-9]' matches all characters in the set of numbers 0 to 9
     '[A-Z]' matches all characters in the set of A to Z
 
=======
     '{2-4}' previous character must match exactly 2-4 times  
>>>>>>> 27283e2422d4773456419bf7cb8ee6845a54aff6
'''

data = '''2013-01-01
2012-02-02
aaaa-02-02
aa-02-02
-04-04
2000 02-02
ghi stu
2012-03-03'''.strip().split('\n')


# A >> '*' matches all characters that follow (0 or more)
print (50*'-' + '\nA\n' + 50*'-')

for line in data:
    match = re.search('(.*)-(..)-(..)', line)    # note the parantheses
    if match: 
        print(match.group(1), match.group(2), match.group(3))  

'''
--------------------------------------------------
A
--------------------------------------------------
2013 01 01
2012 02 02
aaaa 02 02
aa 02 02
 04 04
2012 03 03
'''


# B >> '+' matches all characters that follow (1 or more)
print (50*'-' + '\nB\n' + 50*'-')

for line in data:
    match = re.search('(.+)-(..)-(..)', line)    # note the parantheses
    if match: 
        print(match.group(1), match.group(2), match.group(3))  

'''
--------------------------------------------------
B
--------------------------------------------------
2013 01 01
2012 02 02
aaaa 02 02
aa 02 02
2012 03 03
'''


# C >> '?' makes the previous character optional
print (50*'-' + '\nC\n' + 50*'-')

for line in data:
    match = re.search('(.+)-?(..)-(..)', line)    # note the parantheses
    if match: 
        print(match.group(1), match.group(2), match.group(3)) 

'''
--------------------------------------------------
C
--------------------------------------------------
2013- 01 01
2012- 02 02
aaaa- 02 02
aa- 02 02
- 04 04
2000  02 02
2012- 03 03
'''

# D >> '{4}' previous character must match exactly 4 times 
print (50*'-' + '\nD\n' + 50*'-')

for line in data:
    match = re.search('(a{4})-(..)-(..)', line)    # note the parantheses
    if match: 
        print(match.group(1), match.group(2), match.group(3)) 

'''
--------------------------------------------------
D
--------------------------------------------------
aaaa 02 02
'''

# E >>'{2-4}' previous character must match exactly 2-4 times
print (50*'-' + '\nE\n' + 50*'-')

for line in data:
    match = re.search('(a{2,4})-(..)-(..)', line)    # note the parantheses
    if match: 
        print(match.group(1), match.group(2), match.group(3)) 

'''
--------------------------------------------------
E
--------------------------------------------------
aaaa 02 02
aa 02 02
'''
