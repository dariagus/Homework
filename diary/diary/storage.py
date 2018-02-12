import os.path as Path
import sqlite3

SQL_SELECT_ALL = '''
    SELECT
        id, title_task, content, status, created, deadline
    FROM
        diary
'''

##SQL_SELECT_TASK_BY_PK = SQL_SELECT_ALL + ' WHERE id=?'
##
##SQL_SELECT_TASK_BY_STATUS = SQL_SELECT_ALL + ' WHERE status=?'

SQL_INSERT_TASK = '''
    INSERT INTO diary (title_task, content, deadline) VALUES (?, ?, ?)
'''

SQL_UPDATE_TASK = '''
    UPDATE diary SET title_task=?, content=?, deadline=? WHERE id=?
'''

SQL_UPDATE_COMPLITE_TASK = '''
    UPDATE diary SET status=? WHERE id=?
'''


def dict_factory(cursor, row):
    d = {}

    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    
    return d


def connect(db_name=None):
    if db_name is None:
        db_name=':memory:'
    conn = sqlite3.connect(db.name)

    return conn


def initialize(conn, creation_scripts=None):
    if creation_script is None:
        creation_script = Path.join(Path.dirname(__file__), 'schema.sql')

    with conn, open(creation_script) as f:
        conn.executescript(f.read())



def display_tasks(conn):
    """ Вывести все задачи на экран """
    with conn:
        cursor = conn.execute(SQL_SELECT_ALL)

    return cursor.fetchall()


def add_task(conn, title_task, content, deadline):
    """ Добавляет задачу в БД """
    with conn:
        cursor = conn.execute(SQL_INSERT_TASK, (title_task, content, deadline))

    pk = cursor.lastrowid
    return pk


def edit_task(conn, title_task, content, deadline, pk):
    """ Редактирует задачу в БД """
    with conn:
        cursor = conn.execute(SQL_UPDATE_TASK, (title_task, content, deadline, pk))


def complite_task(conn, pk):
    """ Обновить статус задачи """
    with conn:
        conn.execute(SQL_UPDATE_COMPLITE_TASK, (1, pk))
        
 
def restart_task(conn, pk):
    """ Перезапустить задачу """
    with conn:
        conn.execute(SQL_UPDATE_COMPLITE_TASK, (0, pk))
        

def delete_task(conn, pk):
    """ Удалить задачу """
    with conn:
        conn.execute(SQL_DELETE_TASK_BY_PK, (pk, ))


    
