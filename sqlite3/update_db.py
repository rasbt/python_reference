# 10/28/2013 Sebastian Raschka
# Syntax basics for updating sqlite3 data bases

import sqlite3

# make connection to existing db
conn = sqlite3.connect('zinc_db1.db')
c = conn.cursor()

# update field (no insert if id doesn't exist)
t = ('NO', 'ZINC00895033', )
c.execute("UPDATE zinc_db1 SET purchasable=? WHERE zinc_id=?", t)
print "Total number of rows changed:", conn.total_changes


# update, or insert when id does not exist
# here: updates rotatable bonds if record with primary key zinc_id exists,<br>  
#     else inserts new record an sets purchasable to 0
c.execute("""INSERT OR REPLACE INTO zinc_db1 (zinc_id, rotatable_bonds, purchasable)
              VALUES ( 'ZINC123456798', 
                3, 
                COALESCE((SELECT purchasable from zinc_db1 WHERE zinc_id = 'ZINC123456798'), 0)
              )""")



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
