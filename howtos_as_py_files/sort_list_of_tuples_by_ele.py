# Sebastian Raschka 09/02/2014
# Sorting a list of tuples by the last last elements of the tuple


# Here, we make use of the "key" parameter of the in-built "sorted()" function 
# (also available for the ".sort()" method), which let's us define a function 
# that is called on every element that is to be sorted. In this case, our 
# "key"-function is a simple lambda function that returns the last item 
# from every tuple.



a_list = [(1,3,'c'), (2,3,'a'), (1,2,'b')]

sorted_list = sorted(a_list, key=lambda e: e[::-1])

print(sorted_list)

# prints [(2, 3, 'a'), (1, 2, 'b'), (1, 3, 'c')]