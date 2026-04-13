import tkinter as tk
from database.db import criar_tabela_tarefas, criar_tabela_usuarios
from services.gerenciador_usuarios import GerenciadorUsuarios
from gui.janela_principal import JanelaPrincipal

def main():
    print("--- Iniciando Sistema ---")
    criar_tabela_usuarios()
    criar_tabela_tarefas()

    gerenciador_usuarios = GerenciadorUsuarios()
    app = JanelaPrincipal(gerenciador_usuarios)
    
    print("--- Sistema Pronto. Abrindo Janela... ---")
    app.mainloop()

if __name__ == "__main__":
    main()
