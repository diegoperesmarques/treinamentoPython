'''
Crie um programa que vai ler vários números e colocar 
em uma lista.

Depois disso, mostre:
a) Quantos números foram digitados;
b) A lista de valores, ordenada de forma decrescente;
c) Se o valor 5 foi digitado e está ou não 
'''
valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Você digitou {len(valores)} elementos: ')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
