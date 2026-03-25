from services.gerenciador import GerenciadorTarefas
from database.db import criar_tabela

def menu():
    print("""
          --- GERENCIADOR ---
          1. Adicionar
          2. Listar
          3. Concluir
          4. Remover
          5. Sair""")
    
def obter_id():
    while True:
        try:
            t_id = int(input("ID: "))
            return t_id
        except ValueError:
            print("❌ ID inválido. Por favor, insira um número válido")

def main():
    criar_tabela()
    app = GerenciadorTarefas()

    while True:
        menu()
        op = input("Escolha uma opção: ")

        if op == "1":
            desc = input("Descrição: ")
            app.adicionar(desc)
            print("✅ Tarefa adicionada encontrada")

        elif op == "2":
            tarefas = app.listar()
            if not tarefas:
                print("Nenhuma tarefa.")
            else:
                for tarefa in tarefas:
                    print(tarefa)
        
        elif op == "3":
                t_id = obter_id()
                result = app.concluir(t_id)

                if result is True:
                    print("✅ Tarefa Concluída!")
                elif result is False:
                    print("⚠ A tarefa já estava concluída!")
                else:
                    print("❌ Tarefa não encontrada.")
        
        elif op == "4":
                t_id = obter_id()
                if app.remover(t_id):
                    print("🗑️ Tarefa Removida!")
                else:
                    print("❌ Tarefa não encontrado.")

        elif op == "5":
            print("👋 Até logo!")
            break
            
        else:
            print("Opção inválida! Por favor, escolha uma opção de 1 a 5.")

if __name__ == "__main__":
    main()
