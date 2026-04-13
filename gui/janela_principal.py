import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from services.gerenciador_tarefas import GerenciadorTarefas


class JanelaPrincipal(tk.Tk):
    def __init__(self, gerenciador_usuarios):
        super().__init__()

        self.gerenciador_usuarios = gerenciador_usuarios
        self.gerenciador_tarefas = None
        self.title("Gerenciador de Tarefas")
        self.geometry("400x400")

        self.login_frame = None
        self.tarefas_frame = None
        self.cadastro_frame = None

        self.iniciar_login()

  
    def iniciar_login(self):
        self.limpar_telas()
        
        self.login_frame = tk.Frame(self)
        self.login_frame.pack(pady=20)

        email_label = tk.Label(self.login_frame, text="Email:")
        email_label.grid(row=0, column=0)
        self.email_entry = tk.Entry(self.login_frame)
        self.email_entry.grid(row=0, column=1)

        senha_label = tk.Label(self.login_frame, text="Senha:")
        senha_label.grid(row=1, column=0)
        self.senha_entry = tk.Entry(self.login_frame, show="*")
        self.senha_entry.grid(row=1, column=1)

        login_button = tk.Button(self.login_frame, text="Login", command=self.login)
        login_button.grid(row=2, columnspan=2, pady=10)

        cadastrar_button = tk.Button(self.login_frame, text="Cadastrar", command=self.iniciar_cadastro)
        cadastrar_button.grid(row=3, columnspan=2)

  
    def login(self):
        print("Tentando logar...")
        email = self.email_entry.get()
        senha = self.senha_entry.get()

        if self.gerenciador_usuarios.login(email, senha):
            messagebox.showinfo("Sucesso", "Login bem-sucedido!")
            self.limpar_telas()
            self.gerenciador_tarefas = GerenciadorTarefas(self.gerenciador_usuarios.obter_usuario_logado())
            self.iniciar_tarefas()
        else:
            messagebox.showerror("Erro", "Credenciais inválidas.")

  
    def iniciar_cadastro(self):
        self.limpar_telas()

        self.cadastro_frame = tk.Frame(self)
        self.cadastro_frame.pack(pady=20)

        nome_label = tk.Label(self.cadastro_frame, text="Nome:")
        nome_label.grid(row=0, column=0)
        self.nome_entry = tk.Entry(self.cadastro_frame)
        self.nome_entry.grid(row=0, column=1)

        email_label = tk.Label(self.cadastro_frame, text="Email:")
        email_label.grid(row=1, column=0)
        self.email_entry = tk.Entry(self.cadastro_frame)
        self.email_entry.grid(row=1, column=1)

        senha_label = tk.Label(self.cadastro_frame, text="Senha:")
        senha_label.grid(row=2, column=0)
        self.senha_entry = tk.Entry(self.cadastro_frame, show="*")
        self.senha_entry.grid(row=2, column=1)

        cadastrar_button = tk.Button(self.cadastro_frame, text="Cadastrar", command=self.cadastrar)
        cadastrar_button.grid(row=3, columnspan=2, pady=20)

        voltar_button = tk.Button(self.cadastro_frame, text="Voltar", command=self.iniciar_login)
        voltar_button.grid(row=4, columnspan=2)

  
    def cadastrar(self):
        nome = self.nome_entry.get()
        email = self.email_entry.get()
        senha = self.senha_entry.get()

        if self.gerenciador_usuarios.cadastrar_usuario(nome, email, senha):
            messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
            self.limpar_telas()
            self.iniciar_login()
        else:
            messagebox.showerror("Erro", "Erro ao cadastrar o usuário.")

  
    def iniciar_tarefas(self):
        self.limpar_telas()

        self.tarefas_frame = tk.Frame(self)
        self.tarefas_frame.pack(pady=20)

        self.lista_tarefas = tk.Listbox(self.tarefas_frame, width=40, height=10)
        self.lista_tarefas.pack(pady=10)

        adicionar_button = tk.Button(self.tarefas_frame, text="Adicionar Tarefa", command=self.adicionar_tarefa)
        adicionar_button.pack()

        concluir_button = tk.Button(self.tarefas_frame, text="Concluir Tarefa", command=self.concluir_tarefa)
        concluir_button.pack()

        remover_button = tk.Button(self.tarefas_frame, text="Remover Tarefa", command=self.remover_tarefa)
        remover_button.pack()

        atualizar_button = tk.Button(self.tarefas_frame, text="Atualizar Tarefas", command=self.listar_tarefas)
        atualizar_button.pack()

        deslogar_button = tk.Button(self.tarefas_frame, text="Deslogar", command=self.deslogar)
        deslogar_button.pack()

        excluir_button = tk.Button(self.tarefas_frame, text="Excluir Conta", command=self.excluir_conta)
        excluir_button.pack()

        self.listar_tarefas()

  
    def adicionar_tarefa(self):
        descricao = simpledialog.askstring("Nova Tarefa", "Digite a descrição da tarefa:")

        if descricao:
            resultado = self.gerenciador_tarefas.adicionar_tarefa(descricao)
            messagebox.showinfo("Resultado", resultado)
            self.listar_tarefas()

  
    def listar_tarefas(self):
        #print("Buscando tarefas no banco...")
        self.lista_tarefas.delete(0, tk.END)

        tarefas = self.gerenciador_tarefas.listar_tarefas()

        if isinstance(tarefas, str):
            messagebox.showinfo("Tarefas", tarefas)
            return

        self.tarefas_cache = tarefas

        for tarefa in tarefas:
            self.lista_tarefas.insert(tk.END, str(tarefa))

  
    def obter_tarefa_selecionada(self):
        try:
            indice = self.lista_tarefas.curselection()[0]
            return self.tarefas_cache[indice]
        except IndexError:
            messagebox.showwarning("Aviso", "Selecione uma tarefa primeiro.")
            return None

  
    def concluir_tarefa(self):
        tarefa = self.obter_tarefa_selecionada()
        if tarefa:
            resultado = self.gerenciador_tarefas.concluir_tarefa(tarefa.id)
            messagebox.showinfo("Resultado", resultado)
            self.listar_tarefas()

    def remover_tarefa(self):
        tarefa = self.obter_tarefa_selecionada()
        if tarefa:
            resultado = self.gerenciador_tarefas.remover_tarefa(tarefa.id)
            messagebox.showinfo("Resultado", resultado)
            self.listar_tarefas()


    def deslogar(self):
        self.gerenciador_tarefas = None
        messagebox.showinfo("Deslogado", "Você saiu da sua conta com sucesso.")
        self.iniciar_login()

  
    def excluir_conta(self):
        resposta = messagebox.askyesno("Confirmar", "⚠️ Isso apagará todos os seus dados. Deseja continuar?")
        
        if resposta:
            resultado = self.gerenciador_usuarios.excluir_conta() 
            messagebox.showinfo("Conta Excluída", resultado)
            
            self.limpar_telas()
            self.iniciar_login()

  
    def limpar_telas(self):
        if self.login_frame:
            self.login_frame.destroy()
            self.login_frame = None

        if self.tarefas_frame:
            self.tarefas_frame.destroy()
            self.tarefas_frame = None

        if self.cadastro_frame:
            self.cadastro_frame.destroy()
            self.cadastro_frame = None

