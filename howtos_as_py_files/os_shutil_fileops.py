# sr 11/19/2013
# common file operations in os and shutil modules

import shutil
import os
 
# Getting files of particular type from directory
files = [f for f in os.listdir(s_pdb_dir) if f.endswith(".txt")]
  
# Copy and move
shutil.copyfile("/path/to/file", "/path/to/new/file") 
shutil.copy("/path/to/file", "/path/to/directory")
shutil.move("/path/to/file","/path/to/directory")
   
# Check if file or directory exists
os.path.exists("file or directory")
os.path.isfile("file")
os.path.isdir("directory")
    
# Working directory and absolute path to files
os.getcwd()
os.path.abspath("file")
