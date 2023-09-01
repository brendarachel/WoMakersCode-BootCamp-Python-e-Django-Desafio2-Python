#Modelagem de Sistema - Banco Delas
from abc import ABC, abstractmethod

class Banco(ABC):
    def __init__(self, nome, telefone, renda_mensal):
        self.nome = nome
        self.telefone = telefone
        self.renda_mensal = renda_mensal
    
class Clientes(Banco):
    def __init__(self, genero, id_cliente):
        super().nome
        self.genero = genero
        self.id_cliente = id_cliente
        super().renda_mensal

    @abstractmethod
    def cheque_especial(self, genero):
        pass

    @abstractmethod
    def fazer_saque():
        pass

    @abstractmethod
    def fazer_deposito():
        pass

class ContaCorrente(Clientes):
    def __init__(self):
        super().id_cliente
    
    @abstractmethod
    def mostrar_saldo():
        pass
    


