#!/usr/bin/env bash
# Sebastian Raschka 05/21/2014
# Shell script that prepends a Python shebang 
# '#!/usr/bin/env python' to all
# Python script files in the current directory
# so that script files can be executed via
# >> myscript.py 
# instead of 
# >> python myscript.py

# prepends '#!/usr/bin/env python' to all .py files

find ./ -maxdepth 1 -name "*.py" -exec sed -i.bak '1i\
#!/usr/bin/env python
' {} \;

# removes temporary files
find . -name "*.bak" -exec rm -rf {} \;

# makes Python scripts executable
chmod ug+x *.py
