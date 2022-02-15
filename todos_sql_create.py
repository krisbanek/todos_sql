import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database
       specified by db_file
   :param db_file: database file
   :return: Connection object or None
   """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    
    return conn

def execute_sql(conn, sql):
    """ Execute sql
    :param conn: Connection object
    :param sql: a SQL script
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(sql)
    except Error as e:
        print(e)

if __name__ == "__main__":

    create_todos_sql = """
    -- todos table
    CREATE TABLE IF NOT EXISTS todos (
        id integer PRIMARY KEY,
        zadanie text NOT NULL,
        opis text,
        status text
    );
    """

    table = "todos"
    db_file = "todos.db"

    with create_connection(db_file) as conn:
        if conn is not None:
            execute_sql(conn, create_todos_sql)

create_connection(db_file)
