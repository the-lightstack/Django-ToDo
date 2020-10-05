import sqlite3
def setup_db():
    conn=sqlite3.connect("ToDo_lists.db")
    c=conn.cursor()

    Q1='CREATE TABLE IF NOT EXISTS lists (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, name TEXT NOT NULL) '
    Q2="CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT,done INTEGER NOT NULL,text_content TEXT NOT NULL,parent_id INTEGER NOT NULL)"#The done integer is suposed to be converted to bool and stores one or zero

    c.execute(Q1)
    conn.commit()
    c.execute(Q2)
    conn.commit()
    conn.close()
def get_lists():
    print("Doing stuff in here!")
    conn=sqlite3.connect("ToDo_lists.db")
    c=conn.cursor()
    class Tasks_list():
        def __init__(self,name,id_):
            self.name=name
            self.id_=id_
    lists_list=[]
    for row in c.execute('SELECT * FROM lists ORDER BY id'):
        lists_list.append(Tasks_list(row[1],row[0]))
        print("..............")
    conn.close()
    return lists_list
def get_list_by_id(list_id):
    conn=sqlite3.connect("ToDo_lists.db")
    c=conn.cursor()
    class Tasks_list():
        def __init__(self,name,id_):
            self.name=name
            self.id_=id_
    c.execute("SELECT * FROM lists WHERE id=?",(list_id,))
    output=c.fetchall()
    print("output:",output)
    ret=Tasks_list(output[0][1],output[0][0])
    return ret
def get_tasks_by_list_id(list_id):
    
    conn=sqlite3.connect("ToDo_lists.db")
    c=conn.cursor()
    tasks=[]
    class Task:
        def __init__(self,id_,done,text,parent_id):
            self.id_=id_
            self.done=bool(done)
            self.text=text
            self.parent_id=parent_id
    for row in c.execute("SELECT * FROM tasks ORDER BY id"):
        if row[3]==list_id:
            tasks.append(Task(row[0],row[1],row[2],row[3]))
    return tasks
    '''
Im going to have a table for the lists and one seperate for all of the tasks.

Every list in the list table contains: id, name
Every task contains:id, text, (bool) done, pointer to its corresponding list

#Have to make sure db gets inited before i do get_lists()
#When adding new lists into db, I have to make sure to do 'insert into lists values(NULL,"...")'

'''


