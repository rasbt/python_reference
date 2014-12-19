#!/usr/bin/env python

# Sebastian Raschka 2014
# Functions to calculate factorial, combinations, and permutations
# bundled in an simple command line interface.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
def combinations(n, r):
    numerator = factorial(n)
    denominator = factorial(r) * factorial(n-r)
    return int(numerator/denominator)
    
def permutations(n, r):
    numerator = factorial(n)
    denominator = factorial(n-r)
    return int(numerator/denominator)

assert(factorial(3) == 6)
assert(combinations(20, 8) == 125970)
assert(permutations(30, 3) == 24360)




if __name__ == '__main__':
    
    import argparse
    parser = argparse.ArgumentParser(
        description='Script to calculate the number of combinations or permutations ("n choose r")',
        formatter_class=argparse.RawTextHelpFormatter,
        
        prog='Combinations',
        epilog='Example: ./combinations.py -c 20 3'
        )

    parser.add_argument('-c', '--combinations', type=int, metavar='NUMBER', nargs=2,
            help='Combinations: Number of ways to combine n items with sequence length r where the item order does not matter.')
    
    parser.add_argument('-p', '--permutations', type=int, metavar='NUMBER', nargs=2, 
            help='Permutations: Number of ways to combine n items with sequence length r where the item order does not matter.')
            
    parser.add_argument('-f', '--factorial', type=int, metavar='NUMBER', help='n! e.g., 5! = 5*4*3*2*1 = 120.')
    
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')

    args = parser.parse_args()
    
    if not any((args.combinations, args.permutations, args.factorial)):
        parser.print_help()
        quit()
    
    if args.factorial:
        print(factorial(args.factorial))
            
    if args.combinations:
        print(combinations(args.combinations[0], args.combinations[1]))

    if args.permutations:
        print(permutations(args.permutations[0], args.permutations[1]))
            
    if args.factorial:
        print(factorial(args.factorial))
            
    

    