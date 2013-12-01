# File system operations using Python
# sr 11/30/2013


import os
import shutil

# working directory
c_dir = os.getcwd()                 # show current working directory
os.listdir(c_dir)                   # shows all files in the working directory
os.chdir('~/Data')                  # change working directory



# walk
tree = os.walk(c_dir)      
# moves through sub directories and creates a 'generator' object of tuples
# ('dir', [file1, file2, ...] [subdirectory1, subdirectory2, ...]), 
#    (...), ...



#check files: returns either True or False
os.exists('../rel_path')
os.exists('/home/abs_path')
os.isfile('./file.txt')
os.isdir('./subdir')



# file permission (True or False
os.access('./some_file', os.F_OK) # File exists? Python 2.7
os.access('./some_file', os.R_OK) # Ok to read? Python 2.7
os.access('./some_file', os.W_OK) # Ok to write? Python 2.7
os.access('./some_file', os.X_OK) # Ok to execute? Python 2.7
os.access('./some_file', os.X_OK | os.W_OK) # Ok to execute or write? Python 2.7



# join (creates operating system dependent paths)
os.path.join('a', 'b', 'c')
# 'a/b/c' on Unix/Linux
# 'a\\b\\c' on Windows
os.path.normpath('a/b/c') # converts file separators



# os.path: direcory and file names
os.path.samefile('./some_file', '/home/some_file')  # True if those are the same
os.path.dirname('./some_file')  # returns '.' (everythin but last component)
os.path.basename('./some_file') # returns 'some_file' (only last component
os.path.split('./some_file') # returns (dirname, basename) or ('.', 'some_file)
os.path.splitext('./some_file.txt') # returns ('./some_file', '.txt')
os.path.splitdrive('./some_file.txt') # returns ('', './some_file.txt')
os.path.isabs('./some_file.txt') # returns False (not an absolute path)
os.path.abspath('./some_file.txt')




# create and delete files and directories
os.mkdir('./test')  # create a new direcotory
os.rmdir('./test')  # removes an empty direcotory
os.removedirs('./test') # removes nested empty directories
os.remove('file.txt')   # removes an individual file
shutil.rmtree('./test') # removes directory (empty or not empty)

os.rename('./dir_before', './renamed') # renames directory if destination doesn't exist
shutil.move('./dir_before', './renamed') # renames directory always

shutil.copytree('./orig', './copy') # copies a directory recursively
shutil.copyfile('file', 'copy')     # copies a file

