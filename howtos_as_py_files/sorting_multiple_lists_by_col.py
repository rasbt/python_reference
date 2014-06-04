# Sebastian Raschka 2014

"""
You have 3 lists that you want to sort "relative" to each other,
for example, picturing each list as a row in a 3x3 matrix: sort it by columns

########################
If the input lists are
########################

 list1 = ['c','b','a']
 list2 = [6,5,4]
 list3 = ['some-val-associated-with-c','another_val-b','z_another_third_val-a']

########################
the desired outcome is:
########################

 ['a', 'b', 'c'] 
 [4, 5, 6] 
 ['z_another_third_val-a', 'another_val-b', 'some-val-associated-with-c']

########################
and NOT:
########################

 ['a', 'b', 'c'] 
 [4, 5, 6] 
 ['another_val-b', 'some-val-associated-with-c', 'z_another_third_val-a']


"""

list1 = ['c','b','a']
list2 = [6,5,4]
list3 = ['some-val-associated-with-c','another_val-b','z_another_third_val-a']


list1, list2, list3 = zip(*sorted(zip(list1, list2, list3)))
