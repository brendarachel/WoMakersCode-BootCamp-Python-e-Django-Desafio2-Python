#Modelagem de Sistema - Banco Delas

from abc import ABC, abstractmethod
  
class Clientes(ABC):
    def __init__(self, nome, telefone, renda_mensal):
        self._nome = nome
        self._telefone = telefone
        self.__renda_mensal = renda_mensal

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        if type(novo_nome) != str:
            raise TypeError("Tipo da variável deve ser str")
        self._nome = novo_nome
        
    @property
    def telefone(self):
        return self._telefone
    
    @telefone.setter
    def telefone(self, novo_telefone):
        if type(novo_telefone) != str:
            raise TypeError("Tipo da variável deve ser str")
        self._nome = novo_telefone
    
    @property
    def renda_mensal(self):
        return self.__renda_mensal
    
    @abstractmethod
    def possui_cheque_especial(self):
        pass

class ClienteMulher(Clientes):
    def __init__(self, nome, telefone, renda_mensal):
        super().__init__(nome, telefone, renda_mensal)

    def possui_cheque_especial(self):
        return True

class ClienteHomem(Clientes):
    def __init__(self, nome, telefone, renda_mensal):
        super().__init__(nome, telefone, renda_mensal)

    def possui_cheque_especial(self):
        return False

class ContaCorrente:
    def __init__(self, titular):
        self.__saldo = 0.0
        self.__operacoes = []
        self.__titulares = []
        self.adicionar_titular(titular)

    def adicionar_titular(self, titular):
        self.__titulares.append(titular)

    def fazer_deposito(self, valor: float):
        self.__saldo += valor
        self.__operacoes.append(f'Depósito de R$ {valor:.2f}')

    def fazer_saque(self, valor: float):
        titular = self.__titulares[0]
        if titular.possui_cheque_especial() == False:
            if valor <= self.__saldo:
                self.__saldo -= valor                
                self.__operacoes.append(f'Saque de R$ {valor:.2f}')
            else:
                raise ValueError("Saldo Insuficiente")
        else:
            if valor <= self.__saldo or (self.__saldo - valor) >= -titular.renda_mensal:
                self.__saldo -= valor
                self.__operacoes.append(f'Saque de R$ {valor:.2f}')
            else:
                raise ValueError("Saldo Insuficiente")
    
    @property
    def saldo(self):
        return self.__saldo

    @property
    def operacoes(self):
        return self.__operacoes

cliente_mulher = ClienteMulher("Brenda", "123456", 30000)
cliente_homem = ClienteHomem("Daniel", "456789", 1000)

conta1 = ContaCorrente(cliente_mulher)
conta2 = ContaCorrente(cliente_homem)
    
print(f'O saldo inicial da conta é de R$ {conta1.saldo:.2f}')
print(f'O saldo inicial da conta é de R$ {conta2.saldo:.2f}')
print()

conta1.fazer_deposito(30000)
conta2.fazer_deposito(1000)

print(f'O saldo atual da conta é de R$ {conta1.saldo:.2f}')
print(f'O saldo atual da conta é de R$ {conta2.saldo:.2f}')
print()

conta1.fazer_saque(7000)
conta2.fazer_saque(100)

print(f'O saldo atual da conta é de R$ {conta1.saldo:.2f}')
print(f'O saldo atual da conta é de R$ {conta2.saldo:.2f}')
print()

print(conta1.operacoes)
print()
print(conta2.operacoes)
print()
