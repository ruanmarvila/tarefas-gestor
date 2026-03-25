import sqlite3

def conectar():
    return sqlite3.connect("tarefas.db")

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS tarefas(
                   id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                   descricao TEXT NOT NULL,
                   concluida INTEGER NOT NULL
                   )
                   """)
    conn.commit()
    conn.close()
