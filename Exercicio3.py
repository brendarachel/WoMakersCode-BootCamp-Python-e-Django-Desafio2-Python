#Erros e Exceções

#O programa abaixo deve calcular a média dos valores digitados pelo usuário.
#No entanto, ele não está funcionando bem. Você pode consertá-lo?

def calcular_media(valores):
    tamanho = len(valores) #corrigindo de tamanho = 1 para calcular o tamanho da lista de valores
    soma = sum(valores) #corrigindo para a função de calcular a soma dos valores

    media = soma / tamanho
    return media #acrescentando o retorno da função

valores = []
continuar = True
    
while continuar:
    valor = input('Digite um número para entrar na sua média ou "ok" para calcular o valor: ')
        
    if valor.lower() == 'ok':
        continuar = False #corrigindo de false para False
    else: #acrescentando uma lógica para converter o valor em string para float e atualizando a lista de valores
        valor = float(valor)
        valores.append(valor)
    
media = calcular_media(valores)
print()
print('A média calculada para os valores {} foi de {:.1f}'.format(valores, media)) #formatando a média com uma casa decimal
print()
