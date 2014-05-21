# Sebastian Raschka 05/21/2014
# Shell script that prepends a Python shebang 
# `!#/usr/bin/python` to all
# Python script files in the current directory
# so that script files can be executed via
# >> myscript.py 
# instead of 
# >> python myscript.py

find ./ -maxdepth 1 -name "*.py" -exec sed -i.bak '1i\
!#/usr/bin/python
' {} \;

find . -name "*.bak" -exec rm -rf {} \;