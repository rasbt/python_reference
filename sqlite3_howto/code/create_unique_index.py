# Sebastian Raschka, 2014
# Creating an index on a column with unique! values
# Boosts performance for data base operations.

import sqlite3

sqlite_file = 'my_first_db.sqlite'    # name of the sqlite database file
table_name = 'my_table_2'	# name of the table to be created
id_column = 'my_1st_column' # name of the PRIMARY KEY column
new_column = 'unique_names'  # name of the new column
column_type = 'TEXT' # E.g., INTEGER, TEXT, NULL, REAL, BLOB
index_name = 'my_unique_index'  # name for the new unique index

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

# Adding a new column and update some record
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table_name, cn=new_column, ct=column_type))
c.execute("UPDATE {tn} SET {cn}='sebastian_r' WHERE {idf}=123456".\
        format(tn=table_name, idf=id_column, cn=new_column))

# Creating an unique index
c.execute('CREATE INDEX {ix} on {tn}({cn})'\
        .format(ix=index_name, tn=table_name, cn=new_column))

# Dropping the unique index
# E.g., to avoid future conflicts with update/insert functions
c.execute('DROP INDEX {ix}'.format(ix=index_name))

# Committing changes and closing the connection to the database file
conn.commit()
conn.close()
