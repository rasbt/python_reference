# Sebastian Raschka 2014
# Prints Information of a SQLite database.

# E.g.,
#
"""
Total rows: 1

Column Info:
ID, Name, Type, NotNull, DefaultVal, PrimaryKey
(0, 'id', 'TEXT', 0, None, 1)
(1, 'date', '', 0, None, 0)
(2, 'time', '', 0, None, 0)
(3, 'date_time', '', 0, None, 0)

Number of entries per column:
date: 1
date_time: 1
id: 1
time: 1
"""

import sqlite3


def connect(sqlite_file):
    """ Make connection to an SQLite database file """
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    return conn, c


def close(conn):
    """ Commit changes and close connection to the database """
    # conn.commit()
    conn.close()


def total_rows(cursor, table_name, print_out=False):
    """ Returns the total number of rows in the database """
    cursor.execute('SELECT COUNT(*) FROM {}'.format(table_name))
    count = cursor.fetchall()
    if print_out:
        print('\nTotal rows: {}'.format(count[0][0]))
    return count[0][0]


def table_col_info(cursor, table_name, print_out=False):
    """ Returns a list of tuples with column informations:
    (id, name, type, notnull, default_value, primary_key)
    """
    cursor.execute('PRAGMA TABLE_INFO({})'.format(table_name))
    info = cursor.fetchall()

    if print_out:
        print("\nColumn Info:\nID, Name, Type, NotNull, DefaultVal, PrimaryKey")
        for col in info:
            print(col)
    return info


def values_in_col(cursor, table_name, print_out=True):
    """ Returns a dictionary with columns as keys
    and the number of not-null entries as associated values.
    """
    cursor.execute('PRAGMA TABLE_INFO({})'.format(table_name))
    info = cursor.fetchall()
    col_dict = dict()
    for col in info:
        col_dict[col[1]] = 0
    for col in col_dict:
        c.execute('SELECT ({0}) FROM {1} '
                  'WHERE {0} IS NOT NULL'.format(col, table_name))
        # In my case this approach resulted in a
        # better performance than using COUNT
        number_rows = len(c.fetchall())
        col_dict[col] = number_rows
    if print_out:
        print("\nNumber of entries per column:")
        for i in col_dict.items():
            print('{}: {}'.format(i[0], i[1]))
    return col_dict


if __name__ == '__main__':

    sqlite_file = 'my_first_db.sqlite'
    table_name = 'my_table_3'

    conn, c = connect(sqlite_file)
    total_rows(c, table_name, print_out=True)
    table_col_info(c, table_name, print_out=True)
    # next line might be slow on large databases
    values_in_col(c, table_name, print_out=True)

    close(conn)
