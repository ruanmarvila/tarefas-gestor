from services.gerenciador_usuarios import GerenciadosUsuarios
from services.gerenciador_tarefas import GerenciadorTarefas
from database.db import criar_tabela_tarefas, criar_tabela_usuarios

def menu_cadastro():
    print("--- CADASTRO ---")
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")
    return nome, email, senha


def menu_login():
    print(" --- LOGIN --- ")
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")
    return email, senha


def menu_tarefas():
    print("""
--- GERENCIADOR ---
1. Adicionar
2. Listar
3. Concluir
4. Remover
5. Deslogar
6. Excluir Conta
""")
    

def main():
    criar_tabela_usuarios()
    criar_tabela_tarefas()

    gerenciar_usuarios = GerenciadosUsuarios()

    while True:
        escolha = input("Deseja 1. Logar ou 2. Cadastrar? [1/2]: ")
        if escolha == "1":
            email, senha = menu_login()
            if gerenciar_usuarios.login(email, senha):
                print("Login bem-sucedido!")
                break
            else:
                print("Credenciais inválidas.")
        elif escolha == "2":
            nome, email, senha = menu_cadastro()
            if gerenciar_usuarios.cadastrar_usuario(nome, email, senha):
                print("Cadastro realizado com sucesso!")
            else:
                print("Erro ao cadastrar usuário.")
        else:
            print("Opção Inválida. Tente novamente.")

    gerenciar_tarefas = GerenciadorTarefas(gerenciar_usuarios.obter_usuario_logado())

    while True:
        menu_tarefas()
        op = input("Escolha uma opção: ")

        if op == "1":
            desc = input("Descrição: ")
            print(gerenciar_tarefas.adicionar_tarefa(desc))

        elif op == "2":
            tarefas = gerenciar_tarefas.listar_tarefas()
            if isinstance(tarefas, str):
                print(tarefas)
            else:
                for tarefa in tarefas:
                    print(tarefa)
        
        elif op == "3":
                tarefa_id = int(input("ID da tarefa: "))
                print(gerenciar_tarefas.concluir_tarefa(tarefa_id))
        
        elif op == "4":
                tarefa_id = int(input("ID da tarefa: "))
                print(gerenciar_tarefas.remover_tarefa(tarefa_id))
        
        elif op == "5":
            gerenciar_usuarios.logout()
            print("Você foi deslogado com sucesso!")
            break

        elif op == "6":
            confirmar = input("Tem certeza que deseja excluir sua conta? [S/N]").upper()
            if confirmar == "S":
                email = input("Digite seu email: ")
                senha = input("Digite sua senha: ")
                print(gerenciar_usuarios.excluir_conta(email, senha))
            break
            
        else:
            print("Opção inválida! Por favor, escolha uma opção de 1 a 6.")

if __name__ == "__main__":
    main()
