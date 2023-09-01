#Classes e Objetos

#1. Crie uma classe que modele o objeto "carro".
#2. Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade.

class Carro:
    def __init__(self):
        self.ligado = False
        self.cor = 'Cinza'
        self.modelo = 'Duster'
        self.velocidade = 0
        self.velocidade_min = 0
        self.velocidade_max = 200

#3. Um carro tem os seguintes comportamentos: liga, desliga, acelera, desacelera.

    def liga(self):
        self.ligado = True
    
    def desliga(self):
        self.ligado = False
    
    def acelera(self):
        if self.velocidade == self.velocidade_max:
            return
        
        if self.velocidade < self.velocidade_max:
            self.velocidade += 10
    
    def desacelera(self):
        if self.velocidade == self.velocidade_min:
            return
        
        if self.velocidade > self.velocidade_min:
            self.velocidade -= 10
    
    def __str__(self) -> str:
        return f'Modelo: {self.modelo}\n Cor: {self.cor}\n Ligado? {self.ligado}\n Velocidade: {self.velocidade}km/h'

#4. Crie uma instância da classe carro.
carro = Carro()

#5. Faça o carro "andar" utilizando os métodos da sua classe.

carro.liga()

for _ in range(5):
    carro.acelera()

print(carro)
print()
    
#6. Faça o carro "parar" utilizando os métodos da sua classe.

for _ in range(5):
    carro.desacelera()

carro.desliga()

print(carro)