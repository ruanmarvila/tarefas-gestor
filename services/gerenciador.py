from database.db import conectar
from models.tarefas import Tarefa

class GerenciadorTarefas:
    def adicionar(self, descricao):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO tarefas (descricao, concluida) VALUES (?, ?)",
            (descricao, 0)
        )
        conn.commit()
        conn.close()
    
    def listar(self):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tarefas")
        rows = cursor.fetchall()
        conn.close()

        return [Tarefa(id=row[0], descricao=row[1], concluida=bool(row[2])) for row in rows]

    def concluir(self, tarefa_id):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT concluida FROM tarefas WHERE id = ?", (tarefa_id,))
        resultado = cursor.fetchone()

        if resultado is None:
            conn.close()
            return None

        if resultado[0] == 1:
            conn.close()
            return False

        cursor.execute(
            "UPDATE tarefas SET concluida = 1 WHERE id = ?",
            (tarefa_id,)
        )
        conn.commit()
        conn.close()
        return True
    
    def remover(self, tarefas_id):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM tarefas WHERE id = ?", (tarefas_id,))

        if cursor.rowcount == 0:
            conn.close()
            return False

        conn.commit()
        conn.close()
        return True
