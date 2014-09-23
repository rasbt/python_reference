# Generating a bitstring from a Python list or numpy array
# where all postive values -> 1
# all negative values -> 0

def make_bitstring(ary)
    return np.where(ary > 0, 1, 0)


### Example:

ary1 = np.array([1, 2, 0.3, -1, -2])
make_bitstring(ary1)

# returns array([1, 1, 1, 0, 0])