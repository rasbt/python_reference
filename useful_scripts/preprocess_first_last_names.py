# Sebastian Raschka 2014
#
# A Python function to generalize first and last names.
# The typical use case of such a function to merge data that have been collected 
# from different sources (e.g., names of soccer players as shown in the doctest.)
# 

import unicodedata
import string
import re

def preprocess_names(name, output_sep=' ', firstname_output_letters=1):
    """
    Function that outputs a person's name in the format 
    <last_name><separator><firstname letter(s)> (all lowercase)
    
    >>> preprocess_names("Samuel Eto'o")
    'etoo s'
   
    >>> preprocess_names("Eto'o, Samuel")
    'etoo s'
    
    >>> preprocess_names("Eto'o,Samuel")
    'etoo s'
    
    >>> preprocess_names('Xavi')
    'xavi'
    
    >>> preprocess_names('Yaya Touré')
    'toure y'

    >>> preprocess_names('José Ángel Pozo')
    'pozo j'
    
    >>> preprocess_names('Pozo, José Ángel')
    'pozo j'
    
    >>> preprocess_names('Pozo, José Ángel', firstname_output_letters=2)
    'pozo jo'
    
    >>> preprocess_names("Eto'o, Samuel", firstname_output_letters=2)
    'etoo sa'
    
    >>> preprocess_names("Eto'o, Samuel", firstname_output_letters=0)
    'etoo'
    
    >>> preprocess_names("Eto'o, Samuel", output_sep=', ')
    'etoo, s'
    
    """

    # set first and last name positions
    last, first = 'last', 'first'
    last_pos = -1
    
    if ',' in name:
        last, first = first, last
        name = name.replace(',', ' ')
        last_pos = 1
        
    spl = name.split()
    if len(spl) > 2:
        name = '%s %s' % (spl[0], spl[last_pos])    

    # remove accents
    name = ''.join(x for x in unicodedata.normalize('NFKD', name) if x in string.ascii_letters+' ')
    
    # get first and last name if applicable
    m = re.match('(?P<first>\w+)\W+(?P<last>\w+)', name)
    if m:
        output = '%s%s%s' % (m.group(last), output_sep, m.group(first)[:firstname_output_letters])
    else:
        output = name
    return output.lower().strip()
    
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
