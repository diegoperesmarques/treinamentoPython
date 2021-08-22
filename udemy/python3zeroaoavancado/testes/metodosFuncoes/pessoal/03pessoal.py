'''
Escreva uma função Python que aceita uma string e calcule o 
número de maiúsculas e minúsculas:
Exemplo: Olá Sr, Rogers, como você está bem, terça-feira?
'''
def verificaMaiusculaMinuscula(texto):
    quantidadeMaiuscula = 0
    quantidadeMinuscula = 0
    for i in range(0, len(texto)):
        if texto[i:i+1].isupper() == True:
            quantidadeMaiuscula += 1

        if texto[i:i+1].islower() == True:
            quantidadeMinuscula += 1
    
    print(f'Número de maiúsculas: {quantidadeMaiuscula}')
    print(f'Número de minúsculas: {quantidadeMinuscula}')

verificaMaiusculaMinuscula('Olá Sr, Rogers, como você está bem, terça-feira?')
