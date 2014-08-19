# Sebastian Raschka 08/2014

# Lambda functions are just a short-hand way or writing
# short function definitions

def square_root1(x):
    return x**0.5
    
square_root2 = lambda x: x**0.5

assert(square_root1(9) == square_root2(9))