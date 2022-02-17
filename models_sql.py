
import sqlite3
from sqlite3 import Error

class Todos:
    def __init__(self, db_file="todos.db", table="todos"):
        self.todos = None
        self.db_file = db_file
        self.table = table
        try:
            self.todos = sqlite3.connect(db_file)
        except Error as e:
            print(e)
    
    def all(self): #select_all     
        
        """
        Query all rows in the table
        :param conn: the Connection object
        :return:
        """
        print("Test ALL1")
        self.cur = self.todos.cursor()
        print("Test ALL2")
        self.cur.execute(f"SELECT * FROM {self.table}")
        print("Test ALL3")
        self.rows = self.cur.fetchall()
        print("Test ALL4")

        return self.rows
        
    def get(self, **query): #select_where
        """
        Query tasks from table todos with data from **query dict
        :param conn: the Connection object
        :param table: table name
        :param query: dict of attributes and values
        :return:
        """
        cur = self.todos.cursor()
        qs = []
        values = ()
        for k, v in query.items():
            qs.append(f"{k}=?")
            values += (v,)
        q = " AND ".join(qs)
        cur.execute(f"SELECT * FROM todos WHERE {q}", values)
        self.rows = cur.fetchall()
        print("test get")
        return self.rows

    def create(self, data): #add_task
        #data.pop('csrf_token')
        """
        Create a new task into the todos table
        :param conn:
        :param projekt:
        :return: projekt id
        """

        sql = '''INSERT INTO todos(zadanie, opis, status)
             VALUES(?,?,?)'''
        cur = self.todos.cursor()
        cur.execute(sql, data)
        self.todos.commit()
        return cur.lastrowid
            
    #def update(self, id, data): #update
    #    data.pop('csrf_token')

    def update(self, id, **kwargs):
        """
        update task, opis, and status
        :param conn:
        :param table: table name
        :param id: row id
        :return:
        """
        parameters = [f"{k} = ?" for k in kwargs]
        parameters = ", ".join(parameters)
        values = tuple(v for v in kwargs.values())
        values += (id, )

        sql = f''' UPDATE {self.table}
                   SET {parameters}
                   WHERE id = ?'''
        try:
            cur = self.todos.cursor()
            cur.execute(sql, values)
            self.todos.commit()
            print("OK")
        except sqlite3.OperationalError as e:
            print(e)

todos = Todos()
#todos = todos.all()
#data = ("Obiad", "Zupa", "Tak")
#text = 'opis="spagetti"'

#print(todos.get(id = 1))
#print(todos.create(data))
#print(todos.update(5, zadanie="Kolacja", opis= "Owsianka"))
#print(todos.all())