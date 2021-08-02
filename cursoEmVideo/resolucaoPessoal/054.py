'''
crie um programa que leia o ano de nascimento
de sete pessoas. no final, mostre quantas 
pessoas ainda não atingiram a maioridade
e quantas já são maiores
'''
menor = 0
maior = 0
for i in range(1,7):
    ano = int(input('Digite o ano de nascimento da pessoa {}: '.format(i)))
    if (2021 - ano) < 18:
        menor += 1
    else:
        maior += 1

print('{} são maiores de idade e {} são menores de idade'.format(maior, menor))