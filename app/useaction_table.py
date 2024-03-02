import sqlite3
#ele ira conectar nossa tabela com o banco de dados e não ira criar thrad  
conn = sqlite3.connect("db/dbcad.db", check_same_thread= False) 

def create_table():
    c = conn.cursor
    # Oque ira entrar no banco de dados
    c.execute('''CREATE TABLE IF NOT EXISTS users(
        id INTERGER PRIMARY KKEY AUTOINCREMENT,
        email TEXT,
        senha TEXT)''')
    #Importar para o banco de dados
    conn.commit()