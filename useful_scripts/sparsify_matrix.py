# Sebastian Raschka 2014
#
# Sparsifying a matrix by Zeroing out all elements but the top k elements in a row.
# The matrix could be a distance or similarity matrix (e.g., kernel matrix in kernel PCA),
# where we are interested to keep the top k neighbors.

import numpy as np

print('Sparsify a matrix by zeroing all elements but the top 2 values in a row.\n')

A = np.array([[1,2,3,4,5],[9,8,6,4,5],[3,1,7,8,9]])

print('Before:\n%s\n' %A)


k = 2 # keep top k neighbors
for row in A:
    sort_idx = np.argsort(row)[::-1] # get indexes of sort order (high to low)
    for i in sort_idx[k:]:
        row[i]=0
        
print('After:\n%s\n' %A)


"""
Sparsify a matrix by zeroing all elements but the top 2 values in a row.

Before:
[[1 2 3 4 5]
 [9 8 6 4 5]
 [3 1 7 8 9]]

After:
[[0 0 0 4 5]
 [9 8 0 0 0]
 [0 0 0 8 9]]

"""