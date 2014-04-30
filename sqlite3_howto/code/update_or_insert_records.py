# Sebastian Raschka, 2014
# Update records or insert them if they don't exist.
# Note that this is a workaround to accomodate for missing
# SQL features in SQLite.

import sqlite3

sqlite_file = 'my_first_db.sqlite'
table_name = 'my_table_2'
id_column = 'my_1st_column'
column_name = 'my_2nd_column'

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()


# A) Inserts an ID with a specific value in a second column 
try:
    c.execute("INSERT INTO {tn} ({idf}, {cn}) VALUES (123456, 'test')".\
        format(tn=table_name, idf=id_column, cn=column_name))
except sqlite3.IntegrityError:
    print('ERROR: ID already exists in PRIMARY KEY column {}'.format(id_column))

# B) Tries to insert an ID (if it does not exist yet)
# with a specific value in a second column 
c.execute("INSERT OR IGNORE INTO {tn} ({idf}, {cn}) VALUES (123456, 'test')".\
        format(tn=table_name, idf=id_column, cn=column_name))

# C) Updates the newly inserted or pre-existing entry            
c.execute("UPDATE {tn} SET {cn}=('Hi World') WHERE {idf}=(123456)".\
        format(tn=table_name, cn=column_name, idf=id_column))

conn.commit()
conn.close()
