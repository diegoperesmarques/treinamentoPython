'''
Faça um programa que tenha uma lista chamada números e duas funções
chamadas sorteia() e somaPar(). A primeira função vai sortear 5
números e vai colocá-los dentro da lista e a segunda função vai 
mostrar a soma entre todos os valores PARES sorteados pela função
anterior.
'''
from random import randint

numeros = list()

def sorteia():
    for i in range(0, 5):
        numeros.append(randint(1, 10))

def somaPar():
    soma = 0
    sorteia()
    print(numeros)
    for i in range(0, 5):
        if numeros[i] % 2 == 0:
            soma = soma + numeros[i]
    print(soma)

somaPar()