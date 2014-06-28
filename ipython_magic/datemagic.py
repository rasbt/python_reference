""" 
IPython magic function for printing basic information, such as the current date, time,
Python, and IPython version.

Installation: 
    %install_ext https://raw.githubusercontent.com/rasbt/python_reference/master/ipython_magic/datemagic.py

Usage:
    %load_ext datemagic
    
    
    %date

    optional arguments:
     -d, --date      prints date (default)
     -t, --time      print current time
     -s, --datetime  print current time
     -p, --python    prints Python version
     -i, --ipython   prints IPython version
    
"""

import platform
from time import strftime
from platform import python_version

import IPython
from IPython.core.magic import Magics, magics_class, line_magic
from IPython.core.magic_arguments import argument, magic_arguments, parse_argstring

@magics_class
class DateMagic(Magics):
    """ 
    IPython magic function for printing the current date, time, Python,
    and IPython version.
    
    """
    @magic_arguments()
    @argument('-d', '--date', action='store_true', help='prints date (default)')
    @argument('-t', '--time', action='store_true', help='print current time')
    @argument('-s', '--datetime', action='store_true', help='print current time')
    @argument('-p', '--python', action='store_true', help='prints Python version')
    @argument('-i', '--ipython', action='store_true', help='prints IPython version')
    @line_magic
    def date(self, line):
        """ 
        IPython magic function for printing the current date, time, Python,
        and IPython version.
    
        """
        args = parse_argstring(self.date, line)
        out = ''
        if args.date:
            out += strftime('%d/%m/%Y')
        if args.time:
            if out:
                out += ' '
            out += strftime('%H:%M:%S')
        if args.python:
            if out:
                out += '\n'
            out += 'Python %s' %python_version()
        if args.ipython:
            if out:
                out += '\n'
            out += 'IPython %s' %IPython.__version__
        if not out:
            out += strftime('%d/%m/%Y')
        print(out)

def load_ipython_extension(ipython):
    ipython.register_magics(DateMagic)
