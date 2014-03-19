# Sebastian Raschka, 03/2014
# Getting the positions of min and max values in a list

import operator

values = [1, 2, 3, 4, 5]

min_index, min_value = min(enumerate(values), key=operator.itemgetter(1))
max_index, max_value = max(enumerate(values), key=operator.itemgetter(1))

print('min_index:', min_index, 'min_value:', min_value)
print('max_index:', max_index, 'max_value:', max_value)
