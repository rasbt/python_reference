# Sebastian Raschka 03/2014

import gzip
import os

def conc_gzip_files(in_dir, out_file, append=False):
    """ Reads contents from gzipped ASCII or UTF-8 files, decodes them, and
        appends the lines to one output file.

    Keyword arguments:
        in_dir (str): Path of the directory with the gzip-files
        out_file (str): Path to the resulting file
        append (bool): If true, it appends contents to an exisiting file,
             else creates a new output file.

    """
    write_mode = 'w'
    if append:
        write_mode = 'a'
    gzips = [os.path.join(in_dir, i) for i in os.listdir(in_dir) if i.endswith(i)]
    with open(out_file, write_mode) as ofile:
        for f in gzips:
            with gzip.open(f, 'rb') as gzipf:
                for line in gzipf:
                    ofile.write(line.decode())

if __name__ == '__main__':
    conc_gzip_files('/home/usr/my_dir', '/home/usr/test.txt')
