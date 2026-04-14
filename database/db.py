import sqlite3


def conectar():
    conn = sqlite3.connect('gerenciador.db')
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def criar_tabela_usuarios():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios(
                   id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                   nome TEXT NOT NULL,
                   email TEXT NOT NULL UNIQUE,
                   senha TEXT NOT NULL
                   )
                   """)
    conn.commit()
    conn.close()


def criar_tabela_tarefas():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS tarefas(
                   id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                   descricao TEXT NOT NULL,
                   concluida INTEGER NOT NULL,
                   usuario_id INTEGER,
                   FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE
                   )
                   """)
    conn.commit()
    conn.close()

