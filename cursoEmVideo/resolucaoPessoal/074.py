'''
Crie um programa que vai gerar cinco números aletórios e 
colocar em uma tupla.

Depois disso, mostre a listagem de números gerados e também
indique o menor e o maior valor que estão na tupla.
'''
from random import randint
numero1 = randint(1, 20)
numero2 = randint(1, 20)
numero3 = randint(1, 20)
numero4 = randint(1, 20)
numero5 = randint(1, 20)
lista = (numero1, numero2, numero3, numero4, numero5)
menorNumero = maiorNumero = 0
print(f'Os valores sorteados foram ', end='')
for contador in range(0, len(lista)):
    print(f' {lista[contador]} ', end='')
    if contador == 0:
        menorNumero = lista[contador]
    if lista[contador] < menorNumero:
        menorNumero = lista[contador]
    elif lista[contador] > maiorNumero:
        maiorNumero = lista[contador]

print('')
print(f'O menor número é: {menorNumero}')
print(f'O maior número é: {maiorNumero}')