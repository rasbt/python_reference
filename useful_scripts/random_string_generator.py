import string
import random

def rand_string(length):
    """ Generates a random string of numbers, lower- and uppercase chars. """
    return ''.join(random.choice(
            string.ascii_lowercase + string.ascii_uppercase + string.digits)
                   for i in range(length)
            )

if __name__ == '__main__':
    print("Example1:", rand_string(length=4))
    print("Example2:", rand_string(length=8))
    print("Example2:", rand_string(length=16))


    # Example1: 5bVL
    # Example2: oIIg37xl
    # Example2: 7IqDbrf506TatFO9
