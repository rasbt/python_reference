# Python 2.7
# prompt user for file of specific type(s).
# 11/01/13 sebastian raschka

import os.path

def get_filename(file_type):
    '''repeatedly prompts user for a file of specific type.
       arguments:
           file_type: list with accepted file types as strings.
       returns:
           (string): absolute path to the specified input file.
    '''
    while True:
        print "\n\nplease enter a file name, \nor type --help to get"\
                " a list of the accepted file formats"
        file_name = raw_input(": ")
        if file_name == "--help":
            print "\naccepted file format(s): ",
            for f in file_type:
                print f,
            continue        
        if not os.path.isfile(file_name):
            print "\n\nsorry, this file doesn't exist. please try again.\n"
            continue
        if not (file_name.split(".")[-1] in file_type):
            print "\nplease provide a file in correct format."
            continue
        break
    return os.path.abspath(file_name)

#get_filename(["txt", "doc"])


# ===========================
# EXAMPLE
# ===========================

'''
[bash]~/Desktop >python get_filename.py 


please enter a file name, 
or type --help to get a list of the accepted file formats
: --help

accepted file format(s):  txt doc 

please enter a file name, 
or type --help to get a list of the accepted file formats
: test.tx 


sorry, this file doesn't exist. please try again.



please enter a file name, 
or type --help to get a list of the accepted file formats
: test.txt
[bash]~/Desktop >
'''

