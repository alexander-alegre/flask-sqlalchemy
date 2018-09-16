import sqlite3


def create_tables_if_not_exists():
    connection = sqlite3.connect('data.db')

    cursor = connection.cursor()

    create_table_users = '''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER,
            username text NOT NULL,
            password text NOT NULL,
            PRIMARY KEY (id)
        )
  '''

    create_table_items = '''
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER,
            name text NOT NULL,
            price real,
            PRIMARY KEY (id)
        )
    '''

    cursor.execute(create_table_users)
    cursor.execute(create_table_items)

    connection.commit()
    connection.close()
    return print('db tables created')
