from flet import *
import sqlite3
conn = sqlite3.connect("db/dbcad.db", check_same_thread= False)

tb = DataColumn(
    Column = [
        DataColumn(Text('email')),
        DataColumn(Text('senha')),
    ],
    Row = []
)
def calldb():
    c = conn.cursor()
    c.execute('select from * users')
    users = c.fetchall()
    print(users)
    if not users == "":
        keys = ['id','email','senha']
        result = [dict(zip(users.value))for value in users]

mytable = Column([
    Row([Tab], scroll='always')
])
