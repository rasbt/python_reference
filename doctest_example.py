# doctest example
# Sebastian Raschka 11/19/2013

def subtract(a, b):
    """
    Subtracts second from first number and returns result.
    >>> subtract(10, 5)
    5
    >>> subtract(11, 0.7)
    10.3
    """
    return a-b

def hello_world():
    """
    Returns 'Hello, World'
    >>> hello_world()
    "Hello, World"
    >>> hello_world()
    'Hello, World'
    """
    return "Hello, World"


if __name__ == "__main__":  # is 'false' if imported
    import doctest
    doctest.testmod()


""" RESULTS

sebastian ~/Desktop> python3 doctest_example.py 
**********************************************************************
File "doctest_example.py", line 17, in __main__.hello_world
Failed example:
    hello_world()
Expected:
    "Hello, World"
Got:
    'Hello, World'
**********************************************************************
1 items had failures:
    1 of   2 in __main__.hello_world
***Test Failed*** 1 failures.
sebastian ~/Desktop> 

"""
