# Sebastian Raschka 09/02/2014
# Sorting a list of tuples by the last last elements of the tuple

a_list = [(1,3,'c'), (2,3,'a'), (1,2,'b')]

sorted_list = sorted(a_list, key=lambda e: e[::-1])

print(sorted_list)

# prints [(2, 3, 'a'), (1, 2, 'b'), (1, 3, 'c')]