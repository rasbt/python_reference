# sr 10/29/13
# Calculates elapsed CPU time in seconds as float. 

import time

start_time = time.clock()

i = 0
while i < 10000000:
    i += 1

elapsed_time = time.clock() - start_time
print "Time elapsed: {} seconds".format(elapsed_time)

# prints "Time elapsed: 1.06 seconds"
#        on 4 x 2.80 Ghz Intel Xeon, 6 Gb RAM


