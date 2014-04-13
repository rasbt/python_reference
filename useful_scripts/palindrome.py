# Sebastian Raschka 04/2014

def palindrome(my_str):
    """
    Returns True if an input string is a palindrome. Else returns False.
    """
    stripped_str = "".join(l.lower() for l in my_str if l.isalpha())
    return stripped_str == stripped_str[::-1]

if __name__ == '__main__':
    test1 = 'Hello World!'
    test2 = "Go hang a salami. I'm a lasagna hog."
    print('test1', palindrome(test1))
    print('test2',  palindrome(test2))
