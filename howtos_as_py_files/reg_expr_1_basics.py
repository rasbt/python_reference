# Examples for using Python's Regular expression module "re"
# sr 11/30/2013

import re

'''OVERVIEW
     '|' means 'or'
     '.' matches any single character 
     '()' groups into substrings
'''





# read in data
fileobj = '''abc mno
def pqr
ghi stu
jkl vwx'''

data = fileobj.strip().split('\n')


# A >> if 's' in line
print (50*'-' + '\nA\n' + 50*'-')
for line in data:
    if re.search('abc', line):
        print(">>", line)
    else:
        print("  ", line)

'''
--------------------------------------------------
A
--------------------------------------------------
>> abc mno
   def pqr
   ghi stu
   jkl vwx'''



# B >> if 's' in line or 'r' in line
print (50*'-' + '\nB\n' + 50*'-')
for line in data:
    if re.search('abc|efg', line):
        print(">>", line)
    else:
        print("  ", line)

'''
--------------------------------------------------
B
--------------------------------------------------
>> abc mno
   def pqr
   ghi stu
   jkl vwx
---------------'''


# C >> 
# use () to remember which object was found and return a match object
print (50*'-' + '\nC\n' + 50*'-')
for line in data:
    match = re.search('(abc|efg)', line)    # note the parantheses
    if match: 
        print(match.group(1))               # prints 'abc' if found, else None
        # match.group(0) is the whole pattern that matched

'''
--------------------------------------------------
C
--------------------------------------------------
abc'''



# read in data
fileobj = '''2013-01-01
2012-02-02
ghi stu
2012-03-03'''

data = fileobj.strip().split('\n')


# D >> use '.' to match 'any character'
print (50*'-' + '\nD\n' + 50*'-')
for line in data:
    match = re.search('(2012)-(..)-(..)', line)    # note the parantheses
    if match: 
        print(match.group(1), match.group(2), match.group(3))             

'''
--------------------------------------------------
D
--------------------------------------------------
2012 02 02
2012 03 03'''
