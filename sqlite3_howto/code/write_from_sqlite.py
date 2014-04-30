import sqlite3

def create_col_index(db_name, table_name, column_name, index_name):
    '''
    Creates a column index on a SQLite table.
    
    Keyword arguments:
        db_name (str): Path of the .sqlite database file.
        table_name (str): Name of the target table in the SQLite file.
        condition (str): Condition for querying the SQLite database table.
        column_name (str): Name of the column for which the index is created.

    '''

    # Connecting to the database file
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    # Creating the index
    c.execute('CREATE INDEX {} ON {} ({})'.format(index_name, table_name, column_name))

    # Save index and close the connection to the database
    conn.commit()
    conn.close()



def drop_col_index(db_name, index_name):
    '''
    Drops a column index from a SQLite table.
    
    Keyword arguments:
        db_name (str): Path of the .sqlite database file.
        table_name (str): Name of the target table in the SQLite file.
        condition (str): Condition for querying the SQLite database table.
        column_name (str): Name of the column for which the index is dropped.

    '''

    # Connecting to the database file
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    # Drops the index
    c.execute('DROP INDEX {}'.format(index_name))

    # Save index and close the connection to the database
    conn.commit()
    conn.close()



def write_from_query(db_name, table_name, condition, content_column, out_file, fetchmany=False):
    '''
    Writes contents from a SQLite database column to an output file
    
    Keyword arguments:
        db_name (str): Path of the .sqlite database file.
        table_name (str): Name of the target table in the SQLite file.
        condition (str): Condition for querying the SQLite database table.
        content_column (str): Name of the column that contains the content for the output file.
        out_file (str): Path of the output file that will be written.

    '''
    # Connecting to the database file
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    # Querying the database and writing the output file


    # A) using .fetchmany(); recommended for larger databases
    if fetchmany:
        c.execute('SELECT ({}) FROM {} WHERE {}'.format(content_column, table_name, condition))
        with open(out_file, 'w') as outf:
            results = c.fetchmany(fetchmany)
            while results:
                for row in results:
                    outf.write(row[0])
                results = c.fetchmany(fetchmany)

    # B) simple .execute() loop
    else:
        c.execute('SELECT ({}) FROM {} WHERE {}'.format(content_column, table_name, condition))
        with open(out_file, 'w') as outf:
            for row in c:
                outf.write(row[0])

    # Closing the connection to the database
    conn.close()

if __name__ == '__main__':
    write_from_query(
        db_name='my_db.sqlite',
        table_name='my_table',
        condition='variable1=1 AND variable2<=5 AND variable3="Zinc_Plus"',
        content_column='variable4',
        out_file='sqlite_out.txt'
    )
        


