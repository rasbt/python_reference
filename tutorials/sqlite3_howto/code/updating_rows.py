# Sebastian Raschka, 2014
# Updating rows in an existing SQLite database

import sqlite3

sqlite_file = ''
table_name = ''
column_name_1 = ''  
column_name_2 = ''
column_name_3 = ''
value_1 = 'hello world'
value_2 = 12345

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()


# A.1) Updating all rows for a single column

c.execute('UPDATE {dn} SET {cn1}={v1}'.\
        format(dn=table_name, cn1=column_name_1, v1=value1)


# A.2) Updating all rows for 2 columns (same for multiple columns)

c.execute('UPDATE {dn} SET {cn1}={v1}, {cn2}={v2}'.\
        format(dn=table_name, cn1=column_name_1, cn2=column_name_2,
               v1=value1, v2=value2)




# B.1) Updating specific rows that meet a certain criterion
# here: update column_1 with value_1 if row has value_2 in column_2

c.execute('UPDATE {dn} SET {cn1}={v1} WHERE {cn2}={v2}'.\
        format(dn=table_name, cn1=column_name_1, v1=value1)


# B.2) Updating specific rows that meet multiple criteria
# here: update column_1 with value_1 
#    if row has value_2 in column_2
#    and if row has value = 1 in column_3

c.execute('UPDATE {dn} SET {cn1}={v1} WHERE {cn2}={v2} AND {cn3}=1'.\
        format(dn=table_name, cn1=column_name_1, v1=value1, cn3=column_name_3)


conn.commit()
conn.close()
