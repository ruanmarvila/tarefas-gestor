import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
from services.gerenciador_tarefas import GerenciadorTarefas


class JanelaPrincipal(tk.Tk):
    def __init__(self, gerenciador_usuarios):
        super().__init__()

        style = ttk.Style(self)
        style.theme_use("clam")

        bg = "#1e1e1e"
        fg = "#ffffff"
        entry_bg = "#2b2b2b"
        button_bg = "#3a3a3a"

        self.configure(bg=bg)

        style.configure(".", background=bg, foreground=fg)
        style.configure("TLabel", background=bg, foreground=fg)
        style.configure("TFrame", background=bg)
        style.configure("TButton", background=button_bg, foreground=fg)
        style.map("TButton", background=[('active', '#505050')])
        style.configure("TEntry", fieldbackground=entry_bg, foreground=fg)
        
        self.gerenciador_usuarios = gerenciador_usuarios
        self.gerenciador_tarefas = None
        self.title("Gerenciador de Tarefas")
        self.geometry("600x600")

        self.login_frame = None
        self.tarefas_frame = None
        self.cadastro_frame = None

        self.iniciar_login()
    
    def iniciar_login(self):
        self.limpar_telas()
        
        self.login_frame = ttk.Frame(self)
        self.login_frame.pack(pady=20)

        email_label = ttk.Label(self.login_frame, text="Email:")
        email_label.grid(row=0, column=0, padx=5, pady=5)
        self.email_entry = ttk.Entry(self.login_frame)
        self.email_entry.grid(row=0, column=1)

        senha_label = ttk.Label(self.login_frame, text="Senha:")
        senha_label.grid(row=1, column=0)
        self.senha_entry = ttk.Entry(self.login_frame, show="*")
        self.senha_entry.grid(row=1, column=1)

        login_button = ttk.Button(self.login_frame, text="Login", command=self.login)
        login_button.grid(row=2, columnspan=2, pady=10)

        cadastrar_button = ttk.Button(self.login_frame, text="Cadastrar", command=self.iniciar_cadastro)
        cadastrar_button.grid(row=3, columnspan=2)
    
    def login(self):
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

        self.cadastro_frame = ttk.Frame(self)
        self.cadastro_frame.pack(pady=20)

        nome_label = ttk.Label(self.cadastro_frame, text="Nome:")
        nome_label.grid(row=0, column=0)
        self.nome_entry = ttk.Entry(self.cadastro_frame)
        self.nome_entry.grid(row=0, column=1)

        email_label = ttk.Label(self.cadastro_frame, text="Email:")
        email_label.grid(row=1, column=0)
        self.email_entry = ttk.Entry(self.cadastro_frame)
        self.email_entry.grid(row=1, column=1)

        senha_label = ttk.Label(self.cadastro_frame, text="Senha:")
        senha_label.grid(row=2, column=0)
        self.senha_entry = ttk.Entry(self.cadastro_frame, show="*")
        self.senha_entry.grid(row=2, column=1)

        cadastrar_button = ttk.Button(self.cadastro_frame, text="Cadastrar", command=self.cadastrar)
        cadastrar_button.grid(row=3, columnspan=2, pady=20)

        voltar_button = ttk.Button(self.cadastro_frame, text="Voltar", command=self.iniciar_login)
        voltar_button.grid(row=4, columnspan=2)

    def cadastrar(self):
        nome = self.nome_entry.get().strip()
        email = self.email_entry.get().lower().strip()
        senha = self.senha_entry.get().strip()

        if self.gerenciador_usuarios.cadastrar_usuario(nome, email, senha):
            messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
            self.limpar_telas()
            self.iniciar_login()
        else:
            messagebox.showerror("Erro", "Erro ao cadastrar o usuário.")

    def iniciar_tarefas(self):
        self.limpar_telas()

        self.tarefas_frame = ttk.Frame(self)
        self.tarefas_frame.pack(pady=20, fill="both", expand=True)

        ttk.Label(
            self.tarefas_frame,
            text="Gerenciador de Tarefas",
            font=("Arial", 16)
        ).pack(pady=10)

        lista_frame = ttk.Frame(self.tarefas_frame)
        lista_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.lista_tarefas = tk.Listbox(
            self.tarefas_frame, 
            width=40, 
            height=10,
            bg="#2b2b2b",
            fg="#ffffff",
            selectbackground="#505050",
            selectforeground="#ffffff",
            highlightthickness=0,
            bd=0
            )

        scrollbar = ttk.Scrollbar(
            lista_frame,
            orient="vertical",
            command=self.lista_tarefas.yview
        )

        self.lista_tarefas.config(yscrollcommand=scrollbar.set)
        self.lista_tarefas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        acoes_frame = ttk.LabelFrame(self.tarefas_frame, text="Ações")
        acoes_frame.pack(pady=10, fill="x", padx=10)

        botoes_frame = ttk.Frame(acoes_frame)
        botoes_frame.pack(pady=5)

        ttk.Button(botoes_frame, text="Adicionar", command=self.adicionar_tarefa)\
            .grid(row=0, column=0, padx=5, pady=5)

        ttk.Button(botoes_frame, text="Editar", command=self.editar_tarefas)\
            .grid(row=0, column=1, padx=5, pady=5)

        ttk.Button(botoes_frame, text="Concluir", command=self.concluir_tarefa)\
            .grid(row=0, column=2, padx=5, pady=5)

        ttk.Button(botoes_frame, text="Remover", command=self.remover_tarefa)\
            .grid(row=1, column=0, padx=5, pady=5)

        ttk.Button(botoes_frame, text="Filtrar", command=self.filtrar_tarefas)\
            .grid(row=1, column=1, padx=5, pady=5)

        ttk.Button(botoes_frame, text="Ordenar", command=self.ordenar_tarefas)\
            .grid(row=1, column=2, padx=5, pady=5)

        ttk.Button(acoes_frame, text="Atualizar", command=self.listar_tarefas)\
            .pack(pady=5)

        conta_frame = ttk.LabelFrame(self.tarefas_frame, text="Conta")
        conta_frame.pack(pady=10, fill="x", padx=10)

        ttk.Button(conta_frame, text="Deslogar", command=self.deslogar)\
            .pack(pady=5)

        ttk.Button(conta_frame, text="Excluir Conta", command=self.excluir_conta)\
            .pack(pady=5)

        self.listar_tarefas()

    def adicionar_tarefa(self):
        descricao = simpledialog.askstring("Nova Tarefa", "Digite a descrição da tarefa:")

        if descricao:
            resultado = self.gerenciador_tarefas.adicionar_tarefa(descricao)
            messagebox.showinfo("Resultado", resultado)
            self.listar_tarefas()

    def editar_tarefas(self):
        tarefa = self.obter_tarefa_selecionada()
        if tarefa:
            descricao = simpledialog.askstring("Nova Descrição", "Digite a nova descrição:")

            if descricao:
                resultado = self.gerenciador_tarefas.editar_tarefas(tarefa.id, descricao)
                messagebox.showinfo("Resultado", resultado)
                self.listar_tarefas()

    def listar_tarefas(self):
        tarefas = self.gerenciador_tarefas.listar_tarefas()

        if isinstance(tarefas, str):
            messagebox.showinfo("Tarefas", tarefas)
            return

        self.atualizar_lista(tarefas)

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
    
    def filtrar_tarefas(self):
        condicao = simpledialog.askstring("Filtro", "Escolha o filtro [Pendente/Concluída]: ")

        if not condicao:
            return
        try:
            condicao = condicao.strip().capitalize()
            tarefas = self.gerenciador_tarefas.filtrar_tarefas(condicao)

            if isinstance(tarefas, str):
                messagebox.showinfo("Tarefas", tarefas)
                return

            self.atualizar_lista(tarefas)
        except Exception:
            self.listar_tarefas()
            
    def ordenar_tarefas(self):
        condicao = simpledialog.askstring("Ordem", "Escolha a ordem [ASC/DESC]: ")

        if not condicao:
            return
        try:
            condicao = condicao.strip().upper()
            tarefas = self.gerenciador_tarefas.ordenar_tarefas(condicao)

            if isinstance(tarefas, str):
                messagebox.showinfo("Tarefas", tarefas)
                return
            
            self.atualizar_lista(tarefas)
        except Exception:
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

    def atualizar_lista(self, tarefas):
        self.lista_tarefas.delete(0, tk.END)

        self.tarefas_cache = tarefas
        
        for tarefa in tarefas:
            self.lista_tarefas.insert(tk.END, str(tarefa))
