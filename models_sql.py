import json
import sqlite3
from sqlite3 import Error

class Todos:
    def __init__(self):
        """ create a database connection to the SQLite database
        specified by db_file
        :param db_file: database file
        :return: Connection object or None
        """
        #conn = None
        self.todos = None
        db_file = "todos.db"
        try:
            #conn = sqlite3.connect(db_file)
            #return conn
            self.todos = sqlite3.connect(db_file)
            #return self.todos
        except Error as e:
            print(e)
    
        #return conn
        #return self.todos

    def all(self): #select_all     
        
        """
        Query all rows in the table
        :param conn: the Connection object
        :return:
        """
        #db_file = "todos.db"
        #self.conn = sqlite3.connect(db_file)
        #cur = self.conn.cursor()
        cur = self.todos.cursor()
        cur.execute("SELECT * FROM todos")
        self.rows = cur.fetchall()

        return self.rows
        
    def get(self, conn, **query): #select_where
        """
        Query tasks from table todos with data from **query dict
        :param conn: the Connection object
        :param table: table name
        :param query: dict of attributes and values
        :return:
        """
        cur = conn.cursor()
        qs = []
        values = ()
        for k, v in query.items():
            qs.append(f"{k}=?")
            values += (v,)
        q = " AND ".join(qs)
        cur.execute("SELECT * FROM todos WHERE {q}", values)
        rows = cur.fetchall()
        return rows
        #return self.todos[id]

    def create(self, data): #add_task
        #data.pop('csrf_token')
        """
        Create a new task into the todos table
        :param conn:
        :param projekt:
        :return: projekt id
        """
        db_file = "todos.db"
        conn = sqlite3.connect(db_file)
        data.pop('csrf_token')
        sql = '''INSERT INTO todos(zadanie, opis, status)
             VALUES(?,?,?)'''
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        return cur.lastrowid

    def save_all(self):
        with open("todos.json", "w") as f:
            json.dump(self.todos, f)
            
    def update(self, id, data): #update
        data.pop('csrf_token')
        self.todos[id] = data
        self.save_all()

    #db_file = "todos.db"
    #conn = create_connection(db_file)
    #if __name__ == "__main__":    
        #conn = create_connection(db_file)
        #todos = conn
        #conn.close()

todos = Todos()