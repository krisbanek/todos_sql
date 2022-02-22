
import sqlite3
from sqlite3 import Error
from typing import List

class Todos:
    def __init__(self, db_file="todos.db", table="todos"):
        self.todos = None
        self.db_file = db_file
        self.table = table
        try:
            #self.todos = sqlite3.connect(db_file)
            self.todos = sqlite3.connect(db_file, check_same_thread=False)
        except Error as e:
            print(e)
    
    def all(self): #select_all     
        
        """
        Query all rows in the table
        :param conn: the Connection object
        :return:
        """
        self.cur = self.todos.cursor()
        self.cur.execute(f"SELECT * FROM {self.table}")
        self.rows = self.cur.fetchall()
        
        return self.rows

    def col(self, column): #select_all     
        
        """
        Query all rows in the table
        :param conn: the Connection object
        :return:
        """
        self.column = column
        self.cur = self.todos.cursor()
        self.cur.execute(f"SELECT {column} FROM {self.table}")
        self.rows = self.cur.fetchall()
        
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
        return self.rows

    def get_by_id(self, id):
        """
        Query tasks by priority
        :param conn: the Connection object
        :param status:
        :return:
        """
        self.id = id
        cur1 = self.todos.cursor()
        cur1.execute("SELECT zadanie FROM todos WHERE id=?", (self.id,))
        c1 = cur1.fetchone()[0]


        cur2 = self.todos.cursor()
        cur2.execute("SELECT opis FROM todos WHERE id=?", (self.id,))
        c2 = cur2.fetchone()[0]

        cur3 = self.todos.cursor()
        cur3.execute("SELECT status FROM todos WHERE id=?", (self.id,))
        c3 = cur3.fetchone()[0]

        self.get_dict = {'zadanie':c1, 
                    'opis':c2,
                    'status':c3
                    }

        #self.rows = cur.fetchall()
        return self.get_dict

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
#data = {'zadanie':"Sniadanie", 'opis':"Kanapki", 'status':"Tak"}
#data_list = (data["zadanie"], data["opis"], data["status"])
#print(data_list)
#text = 'opis="spagetti"'

#print(todos.get(id = 2))
#print(todos.create(data.values()))
#todos.update(8, zadanie="auto", opis= "umyc", status="Tak")
#print(todos.all())
#print(todos.col())
#print(todos.get_by_id(2))

#a = todos.get_by_id(2)
#print(todos.get_by_id(2).values())
#get_dict = {'id':get_list[0], 'zadanie':get_list[1], 'opis':get_list[2], 'status':get_list[3]}
#print(get_dict.values())