
cimport numpy as np
cimport cython
@cython.boundscheck(False) 
@cython.wraparound(False)
cpdef cython_bubblesort_nomagic(np.ndarray[long, ndim=1] inp_ary):
    """ The Cython implementation of Bubblesort with NumPy memoryview."""
    cdef unsigned long length, i, swapped, ele, temp
    cdef long[:] np_ary = inp_ary
    length = np_ary.shape[0]
    swapped = 1
    for i in xrange(0, length):
        if swapped: 
            swapped = 0
            for ele in xrange(0, length-i-1):
                if np_ary[ele] > np_ary[ele + 1]:
                    temp = np_ary[ele + 1]
                    np_ary[ele + 1] = np_ary[ele]
                    np_ary[ele] = temp
                    swapped = 1
    return inp_ary