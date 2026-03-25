class Tarefa:
    def __init__(self, id, descricao, concluida=False):
        self.id = id
        self.descricao = descricao
        self.concluida = concluida
    
    def __str__(self):
        status = "✔" if self.concluida else " "
        return f"{self.id}. [{status}] {self.descricao}"
