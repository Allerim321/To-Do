from Dao import *

class ToDo():
    def __init__(self, tarefa=str):
        self.tarefa = tarefa

    def AdicionarTarefa(self, tarefa, idtarefa):
        daoAdicionar = DaoAdicionarTarefa()
        return daoAdicionar.adicionar_tarefa(tarefa, idtarefa)
        
    def ListarTarefas(self):
        return DaoListarTarefa.listar()

    def RemoverTarefa(self, idexcluir):
        return DaoExcluirTarefa.excluir(idexcluir)

TODO = ToDo()
