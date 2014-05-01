# Sebastian Raschka, 03/2014
# comparing string formating: %s and .format()

import timeit

format_res = timeit.timeit("['{}'.format(i) for i in range(10000)]", number=1000)

binaryop_res = timeit.timeit("['%s' %i for i in range(10000)]", number=1000)

print('{}: {}\n{}: {}'.format('format()', format_res, '%s', binaryop_res))

################################
# On my machine
################################
#
# Python 3.4.0
# MacOS X 10.9.2
# 2.5 GHz Intel Core i5
# 4 GB 1600 Mhz DDR3
#
################################
# format(): 2.815331667999999
# %s: 1.630353775999538
################################
