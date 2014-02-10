# Sebastian Raschka, 2014
#
# Print lines that are different between 2 files. Insensitive
# to the order of the file contents.

id_set1 = set()
id_set2 = set()

with open('id_file1.txt', 'r') as id_file:
    for line in id_file:
        id_set1.add(line)

with open('id_file2.txt', 'r') as id_file:
    for line in id_file:
        id_set2.add(line)    

diffs = id_set2.difference(id_set1)

for d in diffs:
    print(d)
print("Total differences:",len(diffs))
