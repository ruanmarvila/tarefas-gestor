from database.db import conectar
from models.usuarios import Usuario

class GerenciadosUsuarios:
    def __init__(self):
        self.usuario_logado = None


    def cadastrar_usuario(self, nome, email, senha):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM usuarios WHERE email = ?", (email,))
        if cursor.fetchone():
            conn.close()
            return False

        cursor.execute("""INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)""",
                       (nome, email, senha))
        
        conn.commit()
        conn.close()
        return True

    def login(self, email, senha):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM usuarios WHERE email = ? AND senha = ?", (email, senha))
        usuario = cursor.fetchone()

        if usuario:
            self.usuario_logado = Usuario(id=usuario[0], nome=usuario[1], email=usuario[2], senha=usuario[3])
            conn.close()
            return True
        conn.close()
        return False

    def logout(self):
        self.usuario_logado = None
        return True

    def obter_usuario_logado(self):
        return self.usuario_logado

    def excluir_conta(self, email, senha):
        conn = conectar()
        conn.execute("PRAGMA foreign_keys = ON")
        cursor = conn.cursor()
        
        if not self.usuario_logado:
            return "Nenhum usuário logado."
        cursor.execute("DELETE FROM usuarios WHERE id = ? AND email = ? AND senha = ?",
                       (self.usuario_logado.id, email, senha))
        if cursor.rowcount == 0:
                conn.close()
                return "Não foi possível excluir o usuário."
        
        conn.commit()
        conn.close()
        return "Usuário excluído com sucesso."
