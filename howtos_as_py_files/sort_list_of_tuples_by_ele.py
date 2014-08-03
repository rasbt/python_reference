# Sebastian Raschka 09/02/2014
# Sorting a list of tuples by starting with the last element of the tuple (=reversed tuple)

# Here, we make use of the "key" parameter of the in-built "sorted()" function 
# (also available for the ".sort()" method), which let's us define a function 
# that is called on every element that is to be sorted. In this case, our 
# "key"-function is a simple lambda function that returns the last item 
# from every tuple.


a_list = [(1,3,'c'), (2,3,'a'), (3,2,'b'), (2,2,'b')]

sorted_list = sorted(a_list, key=lambda e: e[::-1])

print(sorted_list)

# prints [(2, 3, 'a'), (2, 2, 'b'), (3, 2, 'b'), (1, 3, 'c')]



# If we are only interesting in sorting the list by the last element
# of the tuple and don't care about a "tie" situation, we can also use
# the index of the tuple item directly instead of reversing the tuple 
# for efficiency.



a_list = [(1,3,'c'), (2,3,'a'), (3,2,'b'), (2,2,'b')]

sorted_list = sorted(a_list, key=lambda e: e[-1])

print(sorted_list)

# prints [(2, 3, 'a'), (3, 2, 'b'), (2, 2, 'b'), (1, 3, 'c')]