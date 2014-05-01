# Getting command line arguments via sys.arg
# sr 11/30/2013

import sys

def error(msg):
    """Prints error message, sends it to stderr, and quites the program."""
    sys.exit(msg)


args = sys.argv[1:]     #  sys.argv[0] is the name of the python script itself

try:
    arg1 = int(args[0])
    arg2 = args[1]
    arg3 = args[2]
    print("Everything okay!")

except ValueError:
    error("First argument must be integer type!")

except IndexError:
    error("Requires 3 arguments!")

