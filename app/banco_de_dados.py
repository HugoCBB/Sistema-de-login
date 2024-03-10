import sqlite3
conn = sqlite3.connect("db/dbcad.db", check_same_thread= False)

def create_table():
    con = conn.cursor()
    con.execute(''' CREATE TABLE IF NOT EXISTS "users"(
                   "email" TEXT,
                   "senha" TEXT
                )''')
    conn.commit()