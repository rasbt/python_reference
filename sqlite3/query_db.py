# 10/28/2013 Sebastian Raschka
# Syntax basics for querying sqlite3 data bases

import sqlite3

# open existing database
conn = sqlite3.connect('zinc_db1.db')    
c = conn.cursor()

# print all lines ordered by number of non_rot_bonds
for row in c.execute('SELECT * FROM zinc_db1 ORDER BY non_rot_bonds'):
    print row

# print all lines that are purchasable and have <= 7 rotatable bonds
t = ('YES',7,)
for row in c.execute('SELECT * FROM zinc_db1 WHERE purchasable=? AND non_rot_bonds <= ?', t):
	print row

# print all lines that are purchasable and have <= 7 rotatable bonds
t = ('YES',7,)
c.execute('SELECT * FROM zinc_db1 WHERE purchasable=? AND non_rot_bonds <= ?', t)
rows = c.fetchall()
for r in rows:
    print r

# close connection
conn.close()

