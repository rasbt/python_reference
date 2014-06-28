""" 
Sebastian Raschka 2014

datemagic.py
version 1.0.0


IPython magic function for printing basic information, such as the current date, time,
Python, and IPython version.

Installation: 
    %install_ext https://raw.githubusercontent.com/rasbt/python_reference/master/ipython_magic/datemagic.py


Usage:
    %load_ext datemagic
    
    
  %date [-d] [-dd] [-t] [-s] [-z] [-y] [-i] [-p PACKAGES]

 
    IPython magic function for printing the current date, time, Python,
    and IPython version.

    optional arguments:
      -d, --date            prints date (default)
      -dd, --dateday        prints date with abbrv. day and month names
      -t, --time            print current time
      -s, --datetime        print current time
      -z, --timezone        prints time zone
      -y, --python          prints Python version
      -i, --ipython         prints IPython version
      -p PACKAGES, --packages PACKAGES
                        prints versions of Python modules and packages
    
"""

import platform
from pkg_resources import get_distribution
from multiprocessing import cpu_count

import IPython
from IPython.core.magic import Magics, magics_class, line_magic
from IPython.core.magic_arguments import argument, magic_arguments, parse_argstring

@magics_class
class WaterMark(Magics):
    """ 
    IPython magic function for printing the current date, time, Python,
    and IPython version.
    
    """
    @magic_arguments()
    @argument('-d', '--date', action='store_true', help='prints current date')
    @argument('-n', '--datename', action='store_true', help='prints date with abbrv. day and month names')
    @argument('-t', '--datetime', action='store_true', help='prints currenttime')
    @argument('-u', '--custom_time', type=str, help='prints a valid strftime() string')
    @argument('-v', '--python', action='store_true', help='prints Python and IPython version')
    @argument('-p', '--packages', type=str, help='prints versions of Python modules and packages')
    @argument('-m', '--machine', type='store_true', help='prints system and machine info')
    def watermark(self, line):
        """ 
        IPython magic function for printing the current date, time, Python,
        and IPython version.
    
        """
        args = parse_argstring(self.date, line)


        if not any(vars(args).values()):
             print_customtime('%d/%m/%Y')
             print_pyver(args)
             print_sysinfo()


        def print_customtime(self, ctime):
            print(strftime(ctime))
  
        def print_pack(self):
            out = ''
            packages = args.packages.split(',') 
            for p in packages:
                out += '\n%s' %get_distribution(p).version
            print(out)
            

        def print_pyver(self, args):
            out = ''
            if args.python:
                if out:
                    out += '\n'
                out += 'Python %s' %python_version()
            if args.ipython:
                if out:
                    out += '\n'
                out += 'IPython %s' %IPython.__version__
            print(out)


        def print_datetime(self, args):
            out = ''
            if args.date:
                out += strftime('%d/%m/%Y')
            elif args.dateday:
                out += strftime('%a %b %M %Y')
            if args.time:
                if out:
                    out += ' '
                out += strftime('%H:%M:%S')
            if args.timezone:
                if out:
                    out += ' '
                out += strftime('%Z')
            if args.custom_time:
                if out:
                    out += ' '
                out += strftime(args.custom_time)
            print(out)

        def print_sysinfo(self):
             print('compiler        : %s' %platform.python_compiler())
             print('system     : %s' %platform.system())
             print('release    : %s' %platform.release())
             print('machine    : %s' %platform.machine())
             print('processor  : %s' %platform.processor())
             print('CPU count  : %s' %cpu_count())
             print('interpreter: %s' %platform.architecture()[0])


def load_ipython_extension(ipython):
    ipython.register_magics(DateMagic)
