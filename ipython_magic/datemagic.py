""" 
Sebastian Raschka 2014

watermark.py
version 1.0.0


IPython magic function for printing basic information, such as the current date, time,
Python, and IPython version.

Installation: 
    
"""

import platform
from time import strftime
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
    @argument('-m', '--machine', action='store_true', help='prints system and machine info')
    @line_magic
    def watermark(self, line):
        """ 
        IPython magic function for printing the current date, time, Python,
        and IPython version.
    
        """
        args = parse_argstring(self.watermark, line)


        if not any(vars(args).values()):
             self._print_customtime('%d/%m/%Y %H:%M:%S')
             self._print_pyver(args)
             self._print_sysinfo()


    def _print_customtime(self, ctime):
        print(strftime(ctime))
  
    def _print_pack(self):
        out = ''
        packages = args.packages.split(',') 
        for p in packages:
            out += '\n%s' %get_distribution(p).version
        print(out)
            

    def _print_pyver(self, args):
        print('\nPython %s\nIPython %s' %(
                platform.python_version(), 
                IPython.__version__)
             )


    def _print_datetime(self, args):
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

    def _print_sysinfo(self):
         print('\ncompile    : %s' %platform.python_compiler())
         print('system     : %s' %platform.system())
         print('release    : %s' %platform.release())
         print('machine    : %s' %platform.machine())
         print('processor  : %s' %platform.processor())
         print('CPU count  : %s' %cpu_count())
         print('interpreter: %s' %platform.architecture()[0])


def load_ipython_extension(ipython):
    ipython.register_magics(WaterMark)
