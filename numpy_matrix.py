# numpy matrix operations
# sr 12/01/2013

import numpy

ary1 = numpy.array([1,2,3,4,5])  # must be same type
ary2 = numpy.zeros((3,4))        # 3x4 matrix consisiting of 0s 
ary3 = numpy.ones((3,4))         # 3x4 matrix consisiting of 1s 
ary4 = numpy.identity(3)         # 3x3 identity matrix
ary5 = ary1.copy()               # make a copy of ary1

item1 = ary3[0, 0]  # item in row1, column1

ary2.shape  # tuple of dimensions. Here: (3,4)
ary2.size   # number of elements. Here: 12


ary2_t = ary2.transpose()    # transposes matrix

ary2.ravel()     # makes an array linear (1-dimensional)
                 # by concatenating rows
ary2.reshape(2,6) # reshapes array (must have same dimensions)

ary3[0:2, 0:3]   # submatrix of first 2 rows and first 3 columns 

ary3 = ary3[[2,0,1]]    # re-arrange rows


# element-wise operations

ary1 + ary1
ary1 * ary1
numpy.dot(ary1, ary1)   # matrix/vector (dot) product

numpy.sum(ary1)   # sums up all elements in the array
numpy.mean(ary1)   # average of all elements in the array
