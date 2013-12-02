# 10/28/2013 Sebastian Raschka
# Syntax basics for creating sqlite3 data bases

import sqlite3

# create new db and make connection
conn = sqlite3.connect('zinc_db1.db')    
c = conn.cursor()

# create table
c.execute('''CREATE TABLE zinc_db1
             (zinc_id PRIMARY KEY, purchasable TEXT, non_rot_bonds INT)''')

# Insert one row of data
c.execute("INSERT INTO zinc_db1 VALUES ('ZINC00895032','YES', 4)")

# Insert multiple lines of data
multi_lines =[ ('ZINC00895033','YES', 1),
	       ('ZINC00895034','NO', 0),
	       ('ZINC00895035','YES', 3),
	       ('ZINC00895036','YES', 9),
	       ('ZINC00895037','YES', 10) 
	      ]
c.executemany('INSERT INTO zinc_db1 VALUES (?,?,?)', multi_lines)

# Save (commit) the changes
conn.commit()

# close connection
conn.close()
