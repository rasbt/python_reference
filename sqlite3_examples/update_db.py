# 10/28/2013 Sebastian Raschka
# Syntax basics for updating sqlite3 data bases

import sqlite3

# make connection to existing db
conn = sqlite3.connect('zinc_db1.db')
c = conn.cursor()

# update field
t = ('NO', 'ZINC00895033', )
c.execute("UPDATE zinc_db1 SET purchasable=? WHERE zinc_id=?", t)
print "Total number of rows changed:", conn.total_changes

# delete rows
t = ('NO', )
c.execute("DELETE FROM zinc_db1 WHERE purchasable=?", t)
print "Total number of rows deleted: ", conn.total_changes

# add column
c.execute("ALTER TABLE zinc_db1 ADD COLUMN 'keto_oxy' TEXT")

# save changes
conn.commit()

# print column names
c.execute("SELECT * FROM zinc_db1")
col_name_list = [tup[0] for tup in c.description]
print col_name_list



# close connection
conn.close()
