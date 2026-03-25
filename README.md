# Gerenciador de Tarefas
Este é um sistema simples de gerenciamento de tarefas feito em Python, onde você pode adicionar, listar, concluir e remover tarefas.

## Funcionalidades:
- **Adicionar Tarefa**: Cria novas tarefas com uma descrição.
- **Listar Tarefas**: Visualiza todas as tarefas no sistema.
- **Concluir Tarefa**: Marca tarefas como concluídas.
- **Remover Tarefa**: Exclui tarefas do sistema.

## ⚙️ Como Rodar

### Clone o Repositótio
```bash
git clone https://github.com/SEU_USUARIO/tarefas-gestor.git 
```

### Instale as Dependências
```bash
pip install -r requirements.txt
```

### Crie a Tabela no Banco de Dados
```python
from database.db import criar_tabela
criar_tabela()
```

### Execute o Programa
```bash
python main.py
```

## 🛠️: Próximos Passos
- Adiconar interface com Tkinter;
- Adicionar sistema de login;
- Adiconar filtros e ordenação de tarefas;
- Criar uma API RESTful (FastAPI ou Flask).
