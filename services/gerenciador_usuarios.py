import bcrypt
import re
from database.db import conectar
from models.usuarios import Usuario

class GerenciadorUsuarios:
    def __init__(self):
        self.usuario_logado = None

    @staticmethod
    def validar_email(email):
        regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(regex, email) is not None


    def cadastrar_usuario(self, nome, email, senha):
        if not nome.strip() or not email.strip() or not senha.strip():
            return False
        
        if not GerenciadorUsuarios.validar_email(email):
            return False

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM usuarios WHERE email = ?", (email,))
        if cursor.fetchone():
            conn.close()
            return False

        salt = bcrypt.gensalt()
        hashed_senha = bcrypt.hashpw(senha.encode("utf-8"), salt)

        cursor.execute("""INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)""",
                       (nome, email, hashed_senha))
        
        conn.commit()
        conn.close()
        return True

    def login(self, email, senha):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM usuarios WHERE email = ?", (email,))
        usuario = cursor.fetchone()

        if usuario:
            if bcrypt.checkpw(senha.encode("utf-8"), usuario[3]):
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

    def excluir_conta(self):
        if not self.usuario_logado:
            return "Nenhum usuário logado."

        conn = conectar()
        cursor = conn.cursor()
        
        cursor.execute("DELETE FROM usuarios WHERE id = ?", (self.usuario_logado.id,))
        
        conn.commit()
        conn.close()
        self.logout()
        return "Usuário excluído com sucesso."
