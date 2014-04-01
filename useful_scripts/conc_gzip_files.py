# Sebastian Raschka 03/2014

import gzip
import shutil
import os

#import pyprind

def conc_gzip_files(in_dir, out_file, append=False, print_progress=True):
    """ Reads contents from gzipped ASCII or UTF-8 files, decodes them, and
        appends the lines to one output file.

    Keyword arguments:
        in_dir (str): Path of the directory with the gzip-files
        out_file (str): Path to the resulting file
        append (bool): If true, it appends contents to an exisiting file,
             else creates a new output file.
        print_progress (bool): prints progress bar if true.

    """
    write_mode = 'wb'
    gzips = [os.path.join(in_dir, i) for i in os.listdir(in_dir) if i.endswith('.gz')]
    #if print_progress:
    #    pbar = pyprind.ProgBar(len(gzips))
    with open(out_file, 'ab' if append else 'wb') as ofile:
        for f in gzips:
            with gzip.open(f, 'rb') as gzipf:
                shutil.copyfileobj(gzipf, ofile)
            #if print_progress:
            #    pbar.update()

if __name__ == '__main__':
    conc_gzip_files('/home/usr/my_dir', '/home/usr/test.txt')
